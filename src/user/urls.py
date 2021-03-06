from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


from .views import (
 	UserCreateAPIView,
 	UserActivateAPIView,
 	UserLoginAPIView,
 	UserProfileAPIView,
 	UserDetailAPIView
 	)

urlpatterns = [
	
	url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	url(r'^activate/(?P<pk>\d+)/$', UserActivateAPIView.as_view(), name='activate'),
	#url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	url(r'^login/', obtain_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
    url(r'^verify/', verify_jwt_token),
    url(r'^profile/(?P<pk>\d+)/$', UserProfileAPIView.as_view(), name='profile'),

    url(r'^userdetail/(?P<email>[\w.@+-]+)$', UserDetailAPIView.as_view(), name='profile'),
	#(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)
	#url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	#url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	#url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
	# url(r'^(?P<id>\d+)/edit/$', CommentEditAPIView.as_view(), name='edit'),
	#url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),

]