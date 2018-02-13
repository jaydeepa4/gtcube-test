from django.conf.urls import url
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


from .views import (
 	QuestionCreateAPIView,
 	QuestionDetailAPIView,
 	QuestionUpdateAPIView,
 	QuestionDeleteAPIView,
 	QuestionListAPIView,
 	QuestionCategoryCreateAPIView,
 	QuestionCategoryDetailAPIView,
 	QuestionCategoryDetailNameAPIView,
 	QuestionCategoryUpdateAPIView,
 	QuestionCategoryDeleteAPIView,
 	)

urlpatterns = [
	
	# 1. Create new question
	url(r'^qcreate/$', QuestionCreateAPIView.as_view(), name='question_create'),
	#2. Collect the question details based on ID :
	url(r'^qdetail/(?P<pk>\d+)/$', QuestionDetailAPIView.as_view(), name='question_detail'),
	# 3.Update the question details based on ID:
	url(r'^qupdate/(?P<pk>\d+)/$', QuestionUpdateAPIView.as_view(), name='question_update'),
	# 4. Delete the question from the database:
	url(r'^qdelete/(?P<pk>\d+)/$', QuestionDeleteAPIView.as_view(), name='question_delete'),
	# 5. Show the list of all questions based on search parameter created by that seller:
	url(r'^qlist/$', QuestionListAPIView.as_view(), name='question_list'),
	# 6. Exam Category Database - Create new item & Master Item
	url(r'^qccreate/$', QuestionCategoryCreateAPIView.as_view(), name='qc_create'),
	# 7a. Exam Category Database - Collect details about item & Master Item
	url(r'^qcdetail/(?P<pk>\d+)/$', QuestionCategoryDetailAPIView.as_view(), name='qc_detail'),
	# 7a. Exam Category Database - Collect details about item matching exam_name
	url(r'^qcnamedetail/(?P<Exam_Name>\d+)/$', QuestionCategoryDetailNameAPIView.as_view(), name='qc_detail_name'),
	# 8. Exam Category Database - Update details about item & Master Item
	url(r'^qcupdate/(?P<pk>\d+)/$', QuestionCategoryUpdateAPIView.as_view(), name='qc_update'),
	# 9. Exam Category Database - Delete the item & Master Item
	url(r'^qcdelete/(?P<pk>\d+)/$', QuestionCategoryDeleteAPIView.as_view(), name='question_delete'),

	#url(r'^activate/(?P<pk>\d+)/$', SellerActivateAPIView.as_view(), name='activate'),
	#url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	# url(r'^login/', obtain_jwt_token),
 #    url(r'^refresh/', refresh_jwt_token),
 #    url(r'^verify/', verify_jwt_token),
 #    url(r'^profile/(?P<pk>\d+)/$', SellerProfileAPIView.as_view(), name='profile'),

 #    url(r'^sellerdetail/(?P<email>[\w.@+-]+)$', SellerDetailAPIView.as_view(), name='profile'),

 #    url(r'^useremail/$', UserEmailAPIView.as_view(), name='useremail'),

]