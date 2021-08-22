from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE
from django.contrib.auth.models import User
from app_account.models import Profile

from django.conf import settings
# Create your models here.


class City(Model):
  city_name = CharField(max_length=85)
  city_image = CharField(max_length=1000)
  country = CharField(max_length=250)
  
  
  def __str__(self):
      return self.city_name


class Post(Model):
  title = CharField(max_length=150)
  tips = TextField(max_length=10000)
  post_image = CharField(blank=True,max_length=1000)
  post_date = DateTimeField(auto_now_add=True)
  profile = ForeignKey(Profile, on_delete=CASCADE, related_name="posts")
  city = ForeignKey(City, on_delete=CASCADE, related_name="posts")
  
  def __str__(self):
      return self.title