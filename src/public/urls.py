from django.conf.urls import url
from django.contrib import admin

from public.views import (
	course_detail,
	qc_create,
	qc_master,
	qc_update,
	question_create,
	)

urlpatterns = [
	# url(r'^$', post_list, name='list'),
    url(r'^course/(?P<slug>[\w-]+)/$', course_detail, name='detail'),


    #Question Category Creation
    url(r'^qccreate/$', qc_create, name='qc_create'),
    url(r'^qcmaster/$', qc_master, name='qc_master'),
    url(r'^qcupdate/(?P<pk>\d+)/$', qc_update, name='qc_update'),

    #Question -  CRUD
    url(r'^questioncreate/$', question_create, name='question_create'),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
