from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Profile(View):
  
  def get(self, request):
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)

  def post(self, request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("artist_list")
    else:
      context = {"form": form}
      return render(request, "registration/signup.html", context)
  