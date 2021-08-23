from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ChoiceField
from django.contrib.auth.models import User
from app_account.models import Profile
from app_content.models import Post, City


class SignUpForm(UserCreationForm):
  current_city= forms.CharField(help_text='Los Angeles, CA')
  # profile_img = forms.CharField()
  
  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'current_city', 'password1', 'password2',)

class PostCreateForm(ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'tips', 'post_image')


class PostCityCreate(ModelForm):
  
  city = forms.ModelChoiceField(queryset=City.objects.all())
  class Meta:
    model = City
    fields = ('city',)


class UserUpdateForm(ModelForm):
  class Meta:
    model = User
    fields = ('username', 'email', )

class ProfileUpdateForm(ModelForm):
  class Meta:
    model = Profile
    fields = ('current_city', )

