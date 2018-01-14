from django.contrib import admin

from .models import UserProfile
# Register your models here.


class UserProfileModelAdmin(admin.ModelAdmin):
	list_display = ["id", "email", "is_active"]
	
	class Meta:
		model = UserProfile


admin.site.register(UserProfile, UserProfileModelAdmin)