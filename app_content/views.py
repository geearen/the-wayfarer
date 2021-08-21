from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import City, Post, Profile, User
from app_account import views
# Create your views here.


class Home(TemplateView):
  model = City
  template_name="home.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["cities"] = City.objects.all()
    return context

class PostShow(DetailView):
  model = Post
  template_name="post_show.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["profiles"] = Profile.objects.all()
    context["users"] = User.objects.all()
    context["cities"] = City.objects.all()
    context["posts"] = Post.objects.all()
    return context
    
