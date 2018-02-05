from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError, EmailField, CharField, HiddenField, ImageField

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import get_user_model

from django.db.models import Q

from django.utils.crypto import get_random_string

from django.core.mail import send_mail

from django.urls import reverse

from .models import SellerProfile, UserEmail

from post_office import mail


User = get_user_model()

class SellerCreateSerializer(ModelSerializer):
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
		seller_qs = User.objects.filter(email=value)
		if seller_qs.exists():
			raise ValidationError('There is an user/seller existing with this email address')
		return value

	def create(self, validated_data):
		email= validated_data['email']
		password= validated_data['password']
		seller_obj = User (
			email = email
			)
		seller_obj.username = email
		seller_obj.set_password(password)
		seller_obj.save()
		seller_profile_obj = SellerProfile(seller = seller_obj)
		seller_profile_obj.activation_code = get_random_string(length=6, allowed_chars='1234567890')
		seller_profile_obj.is_active = False
		seller_profile_obj.email = email
		seller_profile_obj.save()
		url = reverse('sellers:activate',kwargs={'pk':seller_profile_obj.id})
		#send_mail('Activate your account', 'Click on the link to activate your account :'+url+'/'+'?activation_code='+user_profile_obj.activation_code, 'jaydeepa4@gmail.com',[email], fail_silently=False)
		mail.send(
    		[email], # List of email addresses also accepted
    		'jaydeepa4@gmail.com',
    		subject='My email',
    		message='GTCUBE Activation mail',
    		html_message='<p>Click on the <strong>link</strong> to activate your account :'+url+'?activation_code='+seller_profile_obj.activation_code,
		)
		return validated_data



class UserEmailSerializer(ModelSerializer):
	email = EmailField(label='Email Address')
	class Meta:
		model = UserEmail
		fields = [
			'email',
			]

	def validate_email(self, value):
		data = self.get_initial()
		seller_qs = UserEmail.objects.filter(email=value)
		return value

	def create(self, validated_data):
		email= validated_data['email']
		email_obj = UserEmail (
			email = email
			)
		email_obj.email = email
		email_obj.save()	
		return validated_data



class SellerActivateSerializer(ModelSerializer):
	activation_code = SerializerMethodField()
	class Meta:
		model = SellerProfile
		fields = [
			'email',
			'activation_code',
			'is_active'
			]

	def get_activation_code(self, obj):
		request = self.context['request']
		activation_code_query = request.query_params['activation_code']
		seller_profile_obj = SellerProfile.objects.filter(activation_code = activation_code_query).distinct()
		if seller_profile_obj.exists() and seller_profile_obj.count() == 1:
			seller_profile_obj = seller_profile_obj.first()
			seller_profile_obj.is_active = True
			seller_profile_obj.activation_code = 1
			seller_profile_obj.save()
			return seller_profile_obj.activation_code
		else:
			return 0

class SellerDetailSerializer(ModelSerializer):
	class Meta:
		model = SellerProfile
		fields = [
			'id',
			'email',
			'activation_code',
			'is_active'
			]


class SellerProfileSerializer(ModelSerializer):
	#display_image = ImageField(max_length=None, use_url=True, required=False)
	class Meta:
		model = SellerProfile
		fields = [
			'email',
			'phone',
			'country',
			#'display_image'
		]



# class UserLoginSerializer(ModelSerializer):
# 	email = EmailField(label='Email Address')
# 	token =  SerializerMethodField()
# 	class Meta:
# 		model = User
# 		fields = [
# 			'email',
# 			'password',
# 			'token'
# 			]

# 		extra_kwargs = {'password':
# 							{'write_only':True}
# 						}

# 	def validate(self, data):
# 		user_obj = None
# 		email = data.get('email',None)
# 		username= data.get('email',None)
# 		password =data.get('password',None)

# 		if not email and not username:
# 			raise ValidationError('Please provide Email address to Login')

# 		user = User.objects.filter(
# 			Q(email=email)|
# 			Q(username=username)
# 			).distinct()
# 		user = user.exclude(email__iexact='')
# 		if user.exists() and user.count() ==1:
# 			user_obj = user.first()
# 		else:
# 			raise ValidationError('Incorrect Username/Email address provided.')
# 		if user_obj:
# 			if not user_obj.check_password(password):
# 				raise ValidationError('Incorrect credentials. Please try again')
		
# 		data['token']= 'SOME RANDOM TOKEN'		

# 		return data

# 	def get_token(self, obj):
# 			token= 'SOME RANDOM TOKEN'	
# 			return token