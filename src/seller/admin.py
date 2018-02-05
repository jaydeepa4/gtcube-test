from django.contrib import admin

from .models import SellerProfile, UserEmail
# Register your models here.


class SellerProfileModelAdmin(admin.ModelAdmin):
	list_display = ["id", "email", "is_active"]
	
	class Meta:
		model = SellerProfile

class UserEmailAdmin(admin.ModelAdmin):
	list_display = ["id", "email", "registration_date"]
	
	class Meta:
		model = UserEmail


admin.site.register(SellerProfile, SellerProfileModelAdmin)
admin.site.register(UserEmail, UserEmailAdmin)