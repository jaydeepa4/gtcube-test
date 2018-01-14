from django.db import models

from django.conf import settings
# Create your models here.


#Creating Model for User profile linked to User Model

class UserProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	email = models.EmailField()
	activation_code = models.PositiveIntegerField(blank=True)
	is_active = models.BooleanField()

	class Meta:
		ordering = ['-id']


	def __unicode__(self):  
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

