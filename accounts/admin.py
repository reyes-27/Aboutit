from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
	model=CustomUser
	list_display=['email', 'username', 'birth_date', 'mobile_number', 'is_staff', 'gender',]
	add_form=CustomUserCreationForm
	form=CustomUserChangeForm
	fieldsets=UserAdmin.fieldsets + (
		(None, {'fields':('birth_date', 'mobile_number', 'gender',)}),
		)
	add_fieldsets=UserAdmin.add_fieldsets + (
		(None, {'fields':('birth_date', 'mobile_number', 'gender',)}),
		)


admin.site.register(CustomUser, CustomUserAdmin)