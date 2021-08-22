
from django.urls import path
from django.conf.urls import url
from .views import Signup, ProfileDetail, ProfileUpdate, LoginRedirect
from app_content.views import PostCreate

urlpatterns = [
	path('signup/', Signup.as_view(), name="signup"),
	path('profile/', LoginRedirect.as_view(), name='profile_redirect'),
	path('profile/<int:pk>/', ProfileDetail.as_view(), name="profile_detail"),
	path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name="profile_update"),
]
