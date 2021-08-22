from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .models import City, Post, Profile, User
from django.urls import reverse
from app_account import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator

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
    
class CitiesList(TemplateView):
  pass

class CityDetail(TemplateView):
  pass


class PostCreate(CreateView):
  model = Post
  fields = ['title', 'tips', 'city']
  template_name = 'post_create.html'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(PostCreate, self).form_valid(form)

  def get_success_url(self):
    return reverse("city_detail", kwargs={'pk': self.object.pk})

# @method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
  model = Post
  template_name = "post_delete_confirmation.html"
  success_url = "/cities/"

# @method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
  model = Post
  fields = ['title', 'tips', 'post_image', 'city']
  template_name = "post_update.html"

  def get_success_url(self):
      return reverse("city_detail", kwargs={'pk':self.object.pk})
