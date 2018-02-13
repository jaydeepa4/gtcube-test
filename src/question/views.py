from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView

from .serializers import (
	QuestionCreateSerializer, 
	QuestionDetailSerializer, 
	QuestionUpdateSerializer, 
	QuestionDeleteSerializer, 
	QuestionListSerializer,
	QuestionCategoryCreateSerializer,
	QuestionCategoryDetailSerializer,
	QuestionCategoryUpdateSerializer,
	QuestionCategoryDeleteSerializer,
	)

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

#from posts.api.permissions import IsOwnerOrReadOnly

from rest_framework.filters import SearchFilter, OrderingFilter

from django.db.models import Q

from django.http import Http404

#from posts.api.paginations import PostLimitOffsetPagination, PostPageNumberPagination

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from question.models import QuestionDetails, QuestionCategories

from rest_framework.parsers import MultiPartParser, FormParser

User = get_user_model()

# Create your views here.

# 1. Create new question
class QuestionCreateAPIView(CreateAPIView):
	serializer_class = QuestionCreateSerializer
	queryset = QuestionDetails.objects.all()
	permission_classes = [AllowAny]

#2. Collect the question details based on ID :
class QuestionDetailAPIView(RetrieveAPIView):
	serializer_class = QuestionDetailSerializer
	queryset = QuestionDetails.objects.all()
	lookup_field = 'pk'
	permission_classes = [AllowAny]

# 3.Update the question details based on ID:
class QuestionUpdateAPIView(UpdateAPIView):
	serializer_class = QuestionUpdateSerializer
	queryset = QuestionDetails.objects.all()
	lookup_field = 'pk'
	permission_classes = [AllowAny]


	def put(self, request, pk, format=None):
		question = self.get_object(pk)
		serializer = QuestionUpdateSerializer(question, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get_object(self, pk):
		try:
			return QuestionDetails.objects.get(pk=pk)
		except QuestionDetails.DoesNotExist:
			raise Http404


# 4. Delete the question from the database:
class QuestionDeleteAPIView(DestroyAPIView):
	serializer_class = QuestionUpdateSerializer
	queryset = QuestionDetails.objects.all()
	lookup_field = 'pk'
	permission_classes = [AllowAny]

	def get_object(self, pk):
		try:
			return QuestionDetails.objects.get(pk=pk)
		except QuestionDetails.DoesNotExist:
			raise Http404

	def delete(self, request, pk, format=None):
		QuestionDetails = self.get_object(pk)
		QuestionDetails.delete()
		return Response(status=HTTP_200_OK)


# 5. Show the list of all questions based on search parameter created by that seller:
class QuestionListAPIView(ListAPIView):
	queryset = QuestionDetails.objects.all()
	serializer_class = QuestionListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['Search_Tags','Para_Text', 'Question_Text']


	def get_queryset(self, *args, **kwargs):
		queryset_list = QuestionDetails.objects.all()
		query =self.request.GET.get('q')
		field = self.request.GET.get('field')
		if query:
			if field == 'Search_Tags':
				# Search for search tags :
				queryset_list = queryset_list.filter(
				Q(Search_Tags__icontains=query)).distinct()
			else:
				# Search for Question/Para Text :
				queryset_list = queryset_list.filter(
				Q(Para_Text__icontains=query)|
				Q(Question_Text__icontains=query)
				).distinct()
		return queryset_list

# 6. Exam Category Database - Create new item & Master Item
class QuestionCategoryCreateAPIView(CreateAPIView):
	serializer_class = QuestionCategoryCreateSerializer
	queryset = QuestionCategories.objects.all()
	permission_classes = [AllowAny]

# 7a. Exam Category Database - Collect details about item & Master Item
class QuestionCategoryDetailAPIView(RetrieveAPIView):
	serializer_class = QuestionCategoryDetailSerializer
	queryset = QuestionCategories.objects.all()
	lookup_field = 'pk'
	permission_classes = [AllowAny]

# 7b. Exam Category Database - Collect details about item through exam_name
class QuestionCategoryDetailNameAPIView(RetrieveAPIView):
	serializer_class = QuestionCategoryDetailSerializer
	queryset = QuestionCategories.objects.all()
	lookup_field = 'Exam_Name'
	permission_classes = [AllowAny]

# 8. Exam Category Database - Update details about item & Master Item
class QuestionCategoryUpdateAPIView(UpdateAPIView):
	serializer_class = QuestionCategoryUpdateSerializer
	queryset = QuestionCategories.objects.all()
	lookup_field = 'pk'
	permission_classes = [AllowAny]


	def put(self, request, pk, format=None):
		question = self.get_object(pk)
		serializer = QuestionCategoryUpdateSerializer(question, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get_object(self, pk):
		try:
			return QuestionCategories.objects.get(pk=pk)
		except QuestionCategories.DoesNotExist:
			raise Http404

# 9. Exam Category Database - Delete the item & Master Item
class QuestionCategoryDeleteAPIView(DestroyAPIView):
	serializer_class = QuestionCategoryUpdateSerializer
	queryset = QuestionCategories.objects.all()
	lookup_field = 'pk'
	permission_classes = [AllowAny]

	def get_object(self, pk):
		try:
			return QuestionCategories.objects.get(pk=pk)
		except QuestionCategories.DoesNotExist:
			raise Http404

	def delete(self, request, pk, format=None):
		QuestionCategories = self.get_object(pk)
		QuestionCategories.delete()
		return Response(status=HTTP_200_OK)




# class SellerProfileAPIView(UpdateModelMixin, RetrieveAPIView):
# 	serializer_class = SellerProfileSerializer
# 	queryset = SellerProfile.objects.all()
# 	permission_classes = [AllowAny]
# 	# parser_classes = (MultiPartParser, FormParser,)


# 	def put(self, request, *args, **kwargs):
# 		data = request.data
# 		serializer = SellerProfileSerializer(data=data)
# 		if serializer.is_valid(raise_exception=True):
# 			new_data = serializer.data
# 			return Response(new_data, status=HTTP_200_OK)
# 		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)	
# 		# kwargs['partial'] = True
#   #       return self.update(request, *args, **kwargs)




# class SellerDetailAPIView(RetrieveAPIView):
# 	serializer_class = SellerDetailSerializer
# 	queryset = SellerProfile.objects.all()
# 	lookup_field = 'email'
# 	permission_classes = [AllowAny]


# class UserEmailAPIView(CreateAPIView):
# 	serializer_class = UserEmailSerializer
# 	queryset = UserEmail.objects.all()
# 	permission_classes = [AllowAny]


# class SellerActivateAPIView(RetrieveAPIView):
# 	serializer_class = SellerActivateSerializer
# 	queryset = SellerProfile.objects.all()
# 	permission_classes = [AllowAny]
	


# class SellerLoginAPIView(APIView):
# 	serializer_class = SellerLoginSerializer
# 	permission_classes = [AllowAny]


# 	def post(self, request, *args, **kwargs):
# 		data = request.data
# 		serializer = SellerLoginSerializer(data=data)
# 		if serializer.is_valid(raise_exception=True):
# 			new_data = serializer.data
# 			return Response(new_data, status=HTTP_200_OK)
# 		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)	



   




