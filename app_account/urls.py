
from django.urls import path
from .views import Signup, ProfileDetail, ProfileUpdate

urlpatterns = [
	path('signup/', Signup.as_view(), name="signup"),
	path('<int:pk>/', ProfileDetail.as_view(), name="profile_detail"),
	path('<int:pk>/update/', ProfileUpdate.as_view(), name="profile_update"),
	
]
