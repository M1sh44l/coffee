from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CoffeeBean

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Please enter a valid email.')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class SignInForm(forms.Form):
	username = forms.CharField(max_length=30, required=True)
	password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())


class CoffeeBeanForm(forms.ModelForm):
    class Meta:
        model = CoffeeBean
        fields = ['bean']
