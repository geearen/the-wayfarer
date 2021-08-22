from os import name
from django.urls import path
from .views import Home, PostDetail, PostDelete, PostUpdate
from app_account import views

urlpatterns = [
	path('', Home.as_view(), name="home"),
	path('posts/<int:pk>/', PostDetail.as_view(), name="post_detail"),
	path('posts/<int:pk>/delete/', PostDelete.as_view(), name="post_delete"),
	path('posts/<int:pk>/update/', PostUpdate.as_view(), name="post_update"),
]
