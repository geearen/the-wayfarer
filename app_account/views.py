from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import User, Profile

# Create your views here.

class Signup(View):
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
  