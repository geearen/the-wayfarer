from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.list import ListView

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse
from django.views.generic import DetailView
from .models import City, Post, Profile, User
from app_account import views
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from app_account.forms import PostCreateForm, PostCityCreate
from django.http import HttpResponseRedirect


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
  template_name = 'cities_list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['cities'] = City.objects.all()
    context['posts'] = Post.objects.all()

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['posts'] = Post.objects.all()

    # return context
    

class CityDetail(DetailView):
  model= City
  template_name = "city_detail.html"
    

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['cities'] = City.objects.all()
    context['posts'] = Post.objects.all()
    title_query = self.request.GET.get("title")
    print("==== PPLPLPLPLPLPL =====")

    if title_query != None:
      print("==== YOYOYOYOYOY =====")
      context['posts'] = Post.objects.filter(
        title__icontains = title_query)
    else:
      print("==== :):):) =====")
      context['posts'] = Post.objects.all()

    return context
    


class PostCreate(View):
  def get(self, request,pk):
    p_form = PostCreateForm()
    c_form = PostCityCreate()
    context = {
      "p_form":p_form,
      "c_form":c_form
    }
    return render(request, "post_create.html", context)

  def post(self, request, pk):
    title = request.POST.get('title')
    tips = request.POST.get('tips')
    post_image = request.POST.get('post_image')
    city_pk = request.POST.get('city')
    profile = self.request.user.profile
    post_ = Post.objects.create(title=title, tips=tips, profile=profile, city=City.objects.get(pk=city_pk), post_image=post_image)
    
    return redirect('post_detail', pk=post_.id)

# @method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
  model = Post
  template_name = "post_delete_confirmation.html"
  # success_url = "/cities/"
  def get_success_url(self):
    prof_id = self.request.user.profile.id
    return reverse("profile_detail", kwargs={'pk':prof_id})



# @method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
  model = Post
  fields = ['title', 'tips', 'post_image', 'city']
  template_name = "post_update.html"

  def get_success_url(self):
      return reverse("post_detail", kwargs={'pk':self.object.pk})
