from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import City
from app_account import views
# Create your views here.

class Home(TemplateView):
  model = City
  template_name="home.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["cities"] = City.objects.all()
    return context