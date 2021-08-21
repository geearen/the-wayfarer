from os import name
from django.urls import path
from .views import Home, PostShow

urlpatterns = [
	path('', Home.as_view(), name="home"),
	path('posts/<int:pk>/', PostShow.as_view(), name="post_show"),
]
