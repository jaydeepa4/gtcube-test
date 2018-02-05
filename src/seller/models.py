from django.db import models

from django.conf import settings

from datetime import datetime 
from django.utils import timezone

from django.contrib.auth.models import User, UserManager


# Create your models here.

#Creating Model for Seller profile linked to Seller Model
class SellerProfile(models.Model):
	seller = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	email = models.EmailField()
	activation_code = models.BigIntegerField(blank=True)
	is_active = models.BooleanField()
	phone = models.CharField(max_length = 250,blank=True,default='')
	country = models.CharField(max_length = 250,blank=True,default='')
	display_image = models.ImageField(upload_to = 'sellers/', default='sellers/none/no-img.jpg')

	class Meta:
		ordering = ['-id']


	def __unicode__(self):  
		return str(self.seller.username)

	def __str__(self):
		return str(self.seller.username)


class UserEmail(models.Model):
	email = models.EmailField();
	registration_date = models.DateTimeField(default=datetime.now, blank=True);

	class Meta:
		ordering = ['-id']

	def __unicode__(self):  
		return str(self.email)

	def __str__(self):
		return str(self.email)

