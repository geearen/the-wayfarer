from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField, ForeignKey, CASCADE, OneToOneField
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User

# Create your models here.

class Profile(Model):
  user = ForeignKey(User, on_delete=CASCADE, related_name='profiles')
  profile_img = CharField(max_length=500, default="https://m.media-amazon.com/images/I/61lcM38-tfL._AC_UL1500_.jpg")
  current_city = CharField(max_length=50, default="NA")