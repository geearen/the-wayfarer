
from django.urls import path
from .views import Signup, ProfileDetail, ProfileUpdate
from app_content import views

urlpatterns = [
	path('signup/', Signup.as_view(), name="signup"),
	path('<int:pk>/', ProfileDetail.as_view(), name="profile_detail"),
	path('<int:pk>/update/', ProfileUpdate.as_view(), name="profile_update"),
	path('<int:pk>/', MyLogin.as_view(), name='login'),
]
