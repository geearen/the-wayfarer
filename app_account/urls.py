
from django.urls import path
from .views import Signup, ProfileDetail

urlpatterns = [
	path('signup/', Signup.as_view(), name="signup"),
	path('<int:pk>/', ProfileDetail.as_view(), name="profile_detail"),
]
