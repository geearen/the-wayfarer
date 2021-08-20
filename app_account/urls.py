
from django.urls import path
from .views import Signup, Profile

urlpatterns = [
	path('signup/', Signup.as_view(), name="signup"),
	path('<int:pk>/', Profile.as_view(), name="profile"),
]
