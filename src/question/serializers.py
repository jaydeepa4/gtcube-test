from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ValidationError, EmailField, CharField, HiddenField, ImageField

from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import get_user_model

from django.db.models import Q

from django.utils.crypto import get_random_string

from django.urls import reverse

from .models import QuestionDetails, QuestionCategories

User = get_user_model()

# 1. Create new question
class QuestionCreateSerializer(ModelSerializer):
	class Meta:
		model = QuestionDetails
		fields = [
			'Question_Type',
			'Tags',
			'Para_Text',
			'Question_Text',
			'Options',
			'Answer_Option',
			'Solution',
			'Search_Tags'
			]


	def create(self, validated_data):
		Question_Type= validated_data['Question_Type']
		Tags= validated_data['Tags']
		Para_Text= validated_data['Para_Text']
		Question_Text= validated_data['Question_Text']
		Options= validated_data['Options']
		Answer_Option= validated_data['Answer_Option']
		Solution= validated_data['Solution']
		Search_Tags= validated_data['Search_Tags']
		
		question_obj = QuestionDetails();
		question_obj.Question_Type = Question_Type
		question_obj.Tags = Tags
		question_obj.Para_Text = Para_Text
		question_obj.Question_Text = Question_Text
		question_obj.Options = Options
		question_obj.Answer_Option = Answer_Option
		question_obj.Solution = Solution
		question_obj.Search_Tags = Search_Tags

		#Fetching Seller_Obj from Email as query parameter
		request = self.context['request']
		if request.query_params['seller']:
			email_query = request.query_params['seller']
			seller_obj = User.objects.filter(email = email_query).distinct()
			if seller_obj.exists() and seller_obj.count() == 1: 
				question_obj.seller_obj = seller_obj.first()

		question_obj.save()
		return validated_data


#2. Collect the question details based on ID :

class QuestionDetailSerializer(ModelSerializer):
	class Meta:
		model = QuestionDetails
		fields = [
			'Question_Type',
			'Tags',
			'Para_Text',
			'Question_Text',
			'Options',
			'Answer_Option',
			'Solution',
			'Search_Tags'
			]

# 3.Update the question details based on ID:
class QuestionUpdateSerializer(ModelSerializer):
	class Meta:
			model = QuestionDetails
			fields = [
				'Question_Type',
				'Tags',
				'Para_Text',
				'Question_Text',
				'Options',
				'Answer_Option',
				'Solution',
				'Search_Tags'
				]

# 4. Delete the question from the database:
class QuestionDeleteSerializer(ModelSerializer):
	class Meta:
		model = QuestionDetails
		fields = [
			'id'
			]

# 5. Show the list of all questions based on search parameter created by that seller:
class QuestionListSerializer(ModelSerializer):
	class Meta:
			model = QuestionDetails
			fields = [
				'Question_Type',
				'Tags',
				'Para_Text',
				'Question_Text',
				'Options',
				'Answer_Option',
				'Solution',
				'Search_Tags'
				]

# 6. Exam Category Database - Create new item & Master Item

class QuestionCategoryCreateSerializer(ModelSerializer):
	class Meta:
		model = QuestionCategories
		fields = [
		'Exam_Category',
		'Exam_Name',
		'Exam_Sections',
		'Exam_Topics',
		'Is_Master'
		]


	def create(self, validated_data):
		Exam_Category= validated_data['Exam_Category']
		Exam_Name= validated_data['Exam_Name']
		Exam_Sections= validated_data['Exam_Sections']
		Exam_Topics= validated_data['Exam_Topics']
		if(validated_data['Is_Master']):
			Is_Master= validated_data['Is_Master']
		else:
			Is_Master = False
		question_obj = QuestionCategories();
		question_obj.Exam_Category = Exam_Category
		question_obj.Exam_Name = Exam_Name
		question_obj.Exam_Sections = Exam_Sections
		question_obj.Exam_Topics = Exam_Topics
		question_obj.Is_Master = Is_Master

		question_obj.save()
		return validated_data

# 7. Exam Category Database - Collect details about item & Master Item

class QuestionCategoryDetailSerializer(ModelSerializer):
	class Meta:
		model = QuestionCategories
		fields = [
		'Exam_Category',
		'Exam_Name',
		'Exam_Sections',
		'Exam_Topics',
		'Is_Master'
		]

# 8. Exam Category Database - Update details about item & Master Item
class QuestionCategoryUpdateSerializer(ModelSerializer):
	class Meta:
		model = QuestionCategories
		fields = [
		'Exam_Category',
		'Exam_Name',
		'Exam_Sections',
		'Exam_Topics',
		'Is_Master'
		]

# 9. Exam Category Database - Delete the item & Master Item
class QuestionCategoryDeleteSerializer(ModelSerializer):
	class Meta:
		model = QuestionCategories
		fields = [
			'id'
			]


# class SellerActivateSerializer(ModelSerializer):
# 	activation_code = SerializerMethodField()
# 	class Meta:
# 		model = SellerProfile
# 		fields = [
# 			'email',
# 			'activation_code',
# 			'is_active'
# 			]

# 	def get_activation_code(self, obj):
# 		request = self.context['request']
# 		activation_code_query = request.query_params['activation_code']
# 		seller_profile_obj = SellerProfile.objects.filter(activation_code = activation_code_query).distinct()
# 		if seller_profile_obj.exists() and seller_profile_obj.count() == 1:
# 			seller_profile_obj = seller_profile_obj.first()
# 			seller_profile_obj.is_active = True
# 			seller_profile_obj.activation_code = 1
# 			seller_profile_obj.save()
# 			return seller_profile_obj.activation_code
# 		else:
# 			return 0




# class SellerProfileSerializer(ModelSerializer):
# 	#display_image = ImageField(max_length=None, use_url=True, required=False)
# 	class Meta:
# 		model = SellerProfile
# 		fields = [
# 			'email',
# 			'phone',
# 			'country',
# 			#'display_image'
# 		]
