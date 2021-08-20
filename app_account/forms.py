from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
  current_city= forms.CharField(help_text='Los Angeles, CA')
  # profile_img = forms.CharField()
  
  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'current_city', 'password1', 'password2',)
