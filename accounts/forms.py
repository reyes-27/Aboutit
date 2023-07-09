from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model=CustomUser
		fields=UserCreationForm.Meta.fields + ('mobile_number', 'birth_date',)

class CustomUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model=CustomUser
		fields=UserCreationForm.Meta.fields + ('mobile_number', 'birth_date',)