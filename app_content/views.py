from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
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

class PostDetail(DetailView):
  model = Post
  template_name="post_detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["profiles"] = Profile.objects.all()
    context["users"] = User.objects.all()
    context["cities"] = City.objects.all()
    context["posts"] = Post.objects.all()
    return context

    
class PostCreate(CreateView):
  model = Post
  fields = ['title', 'tips', 'profile', 'city']
  template_name = 'post_create.html'
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(PostCreate, self).form_valid(form)

  def get_success_url(self):
    return reverse("post_create", kwargs={'pk': self.object.pk})
