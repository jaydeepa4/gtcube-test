from django.db import models

from django.conf import settings

from datetime import datetime 
from django.utils import timezone

from django.contrib.auth.models import User, UserManager

# Create your models here.

class QuestionDetails(models.Model):
	seller_obj = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	Question_Type = models.CharField(max_length = 250,blank=True,default='')
	Tags = models.TextField(blank=True,default='')
	Para_Text = models.TextField(blank=True,default='')
	Question_Text = models.TextField(blank=True,default='')
	Options = models.TextField(blank=True,default='')
	Answer_Option = models.CharField(max_length = 250, blank=True,default='')
	Solution = models.TextField(blank=True,default='')
	Search_Tags = models.TextField(blank=True,default='')
	Created_Time = models.DateTimeField(auto_now_add=True, blank=True)
	Updated_Time = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ['-id']


	def __unicode__(self):  
		return str(self.id)

	def __str__(self):
		return str(self.id)


class QuestionCategories(models.Model):
	Exam_Category = models.TextField(blank=True,default='')
	Exam_Name = models.TextField(blank=True,default='')
	Exam_Sections = models.TextField(blank=True,default='')
	Exam_Topics = models.TextField(blank=True,default='')
	Is_Master = models.BooleanField(default=False)
	Created_Time = models.DateTimeField(auto_now_add=True, blank=True)
	Updated_Time = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-id']


	def __unicode__(self):  
		return str(self.id)

	def __str__(self):
		return str(self.id)