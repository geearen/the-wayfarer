from os import name
from django.urls import path
from .views import Home, PostDetail, PostCreate
from app_account import views

urlpatterns = [
	path('', Home.as_view(), name="home"),
	path('posts/<int:pk>/', PostDetail.as_view(), name="post_detail"),
	path('posts/new', PostCreate.as_view(), name='post_create'),
]
