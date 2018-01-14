from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError, EmailField, CharField, HiddenField

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import get_user_model

from django.db.models import Q

from django.utils.crypto import get_random_string

from django.core.mail import send_mail

from django.urls import reverse

from .models import UserProfile


User = get_user_model()

class UserCreateSerializer(ModelSerializer):
	email = EmailField(label='Email Address')
	class Meta:
		model = User
		fields = [
			'email',
			'password'
			]
		extra_kwargs = {'password':
							{'write_only':True}
						}

	def validate_email(self, value):
		data = self.get_initial()
		user_qs = User.objects.filter(email=value)
		if user_qs.exists():
			raise ValidationError('There is an user existing with this email address')
		return value

	def create(self, validated_data):
		email= validated_data['email']
		password= validated_data['password']
		user_obj = User (
			email = email
			)
		user_obj.username = email
		user_obj.set_password(password)
		user_obj.save()
		user_profile_obj = UserProfile(user = user_obj)
		user_profile_obj.activation_code = get_random_string(length=15, allowed_chars='1234567890')
		user_profile_obj.is_active = False
		user_profile_obj.email = email
		user_profile_obj.save()
		url = reverse('users:activate',kwargs={'pk':user_profile_obj.id})
		send_mail('Activate your account', 'Click on the link to activate your account :'+url+'/'+'?activation_code='+user_profile_obj.activation_code, 'jaydeepa4@gmail.com',[email], fail_silently=False)
		return validated_data

class UserActivateSerializer(ModelSerializer):
	activation_code = SerializerMethodField()
	class Meta:
		model = UserProfile
		fields = [
			'email',
			'activation_code',
			'is_active'
			]

	def get_activation_code(self, obj):
		request = self.context['request']
		activation_code_query = request.query_params['activation_code']
		user_profile_obj = UserProfile.objects.filter(activation_code = activation_code_query).distinct()
		if user_profile_obj.exists() and user_profile_obj.count() == 1:
			user_profile_obj = user_profile_obj.first()
			user_profile_obj.is_active = True
			user_profile_obj.activation_code = 1
			user_profile_obj.save()
			return user_profile_obj.activation_code
		else:
			return 0



	token = CharField(allow_blank = True, read_only=True)
	username=CharField()


class UserLoginSerializer(ModelSerializer):
	email = EmailField(label='Email Address')
	token =  SerializerMethodField()
	class Meta:
		model = User
		fields = [
			'email',
			'password',
			'token'
			]

		extra_kwargs = {'password':
							{'write_only':True}
						}

	def validate(self, data):
		user_obj = None
		email = data.get('email',None)
		username= data.get('email',None)
		password =data.get('password',None)

		if not email and not username:
			raise ValidationError('Please provide Email address to Login')

		user = User.objects.filter(
			Q(email=email)|
			Q(username=username)
			).distinct()
		user = user.exclude(email__iexact='')
		if user.exists() and user.count() ==1:
			user_obj = user.first()
		else:
			raise ValidationError('Incorrect Username/Email address provided.')
		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError('Incorrect credentials. Please try again')
		
		data['token']= 'SOME RANDOM TOKEN'		

		return data

	def get_token(self, obj):
			token= 'SOME RANDOM TOKEN'	
			return token