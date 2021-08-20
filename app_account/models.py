from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField, ForeignKey, CASCADE, OneToOneField
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User

# we will now define signals so our Profile model will be automatically created/updated when we create/update User instances.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class Profile(Model):
  user = OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="profile")
  profile_img = CharField(max_length=500, default="https://m.media-amazon.com/images/I/61lcM38-tfL._AC_UL1500_.jpg")
  current_city = CharField(max_length=50, default="NA")

  @receiver(post_save, sender=User)
  def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
  
  
  def __str__(self):
    return self.user.username
