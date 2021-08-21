from os import name
from django.urls import path
from .views import Home, PostDetail
from app_account import views

urlpatterns = [
	path('', Home.as_view(), name="home"),
	path('posts/<int:pk>/', PostDetail.as_view(), name="post_detail"),
]
