from django.db import models

from django.conf import settings

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Create your models here.


#Creating Model for User profile linked to User Model

class UserProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	email = models.EmailField()
	activation_code = models.BigIntegerField(blank=True)
	is_active = models.BooleanField()
	phone = models.CharField(max_length = 250,blank=True,default='')
	country = models.CharField(max_length = 250,blank=True,default='')
	display_image = models.ImageField(upload_to = 'users/', default='users/none/no-img.jpg')

	class Meta:
		ordering = ['-id']


	def __unicode__(self):  
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

