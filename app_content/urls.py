from os import name
from django.urls import path
from .views import Home, PostShow
from app_account import views

urlpatterns = [
	path('', Home.as_view(), name="home"),
	path('posts/<int:pk>/', PostShow.as_view(), name="post_show"),
]
