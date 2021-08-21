from app_account.forms import SignUpForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from .models import User, Profile

# Create your views here.

class Signup(View):
  '''
  model = User, Profile
  fields = ['first_name', 'last_name', 'email', 'current_city', 'profile_img']
  
  def get(self, request):
    form = UserCreationForm()

    context = {"form": form}
    return render(request, "signup.html", context)

  def post(self, request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("signup")
    else:
      context = {"form": form}
      return render(request, "signup.html", context)
  '''
  def get(self, request):
    form = SignUpForm()
    context = {
      "form":form
    }
    return render(request, "signup.html", context)
  
  def post(self,request):
    if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
        user = form.save()
        
        # If you don’t call user.refresh_from_db(), when you try to access the user.profile, it will return None.
        user.refresh_from_db()
        user.profile.current_city = form.cleaned_data.get('current_city')
        # user.profile.profile_img = form.cleaned_data.get('profile_img')
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(request, user)
        return redirect('login')
    else:
      form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class ProfileDetail(DetailView):
  model = Profile
  template_name = "profile_detail.html"

# class UserUpdate(UpdateView):
#   model =  User
#   fields = [ 'username', 'email']
#   template_name = "profile_update.html"

#   def get_success_url(self):
#     return reverse("profile_detail", kwargs={'pk': self.object.pk})

class ProfileUpdate(UpdateView):
  model = User 
  fields = ['username', 'email']
  template_name = "profile_update.html"
  

  # def get_context_data(self, pk, **kwargs):
  #   context = super(ProfileUpdate, self).get_context_data(**kwargs)
  #   context["second_model"] = User.objects.get(pk=pk)
  #   return context

  def get_success_url(self):
    return reverse("profile_detail", kwargs={'pk': self.object.pk})

class LoginRedirect(View):
  
  def get(self, request):
    return redirect(f"/accounts/profile/{request.user.profile.pk}")