from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=False)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	phone_number = forms.CharField(max_length=10, required=False)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(required=False)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']