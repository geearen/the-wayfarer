from django.db.models.fields.related import ForeignKey
from app_account.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from .models import User, Profile
from app_content.models import Post

# Create your views here.

class Signup(View):
  '''
  model = User, Profile
  fields = ['first_name', 'last_name', 'email', 'current_city', 'profile_img']
  
  def get(self, request):
    form = UserCreationForm()

    context = {"form": form}
    return render(request, "signup.html", context)

  def post(self, request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("signup")
    else:
      context = {"form": form}
      return render(request, "signup.html", context)
  '''
  def get(self, request):
    form = SignUpForm()
    context = {
      "form":form
    }
    return render(request, "signup.html", context)
  
  def post(self,request):
    if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
        user = form.save()
        
        # If you don’t call user.refresh_from_db(), when you try to access the user.profile, it will return None.
        user.refresh_from_db()
        user.profile.current_city = form.cleaned_data.get('current_city')
        # user.profile.profile_img = form.cleaned_data.get('profile_img')
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(request, user)
        return redirect('login')
    else:
      form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class ProfileDetail(DetailView):
  model = Profile
  template_name = "profile_detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['posts'] = Post.objects.all()
    

    return context


# class UserUpdate(UpdateView):
#   model =  User
#   fields = [ 'username', 'email']
#   template_name = "profile_update.html"

#   def get_success_url(self):
#     return reverse("profile_detail", kwargs={'pk': self.object.pk})

class ProfileUpdate(View):

  def get(self, request, pk):
      u_form = UserUpdateForm()
      p_form = ProfileUpdateForm()
      context = {
        "u_form":u_form,
        "p_form":p_form
      }
      return render(request, "profile_update.html", context)
  
  def post(self, request, pk):
    username = request.POST.get('username')
    email = request.POST.get('email')
    city = request.POST.get('current_city')
    prof_id = self.request.user.profile.id
    # print(f'======= title: {username} =======')
    # print(f'======= tips: {email} =======')
    # print(f'======= city: {city} =======')
    # print(f'======= profile: {self.request.user.username} =======')
    # # print(f'======= pk: {pk} =======')
    User.objects.filter(username=self.request.user.username).update(username=username, email=email)
    Profile.objects.filter(user=self.request.user.profile.user).update(current_city=city)

    return redirect('profile_detail', pk=prof_id)

  # def get_success_url(self):
  #   return reverse("profile_detail", kwargs={'pk': self.object.profile.pk})




class LoginRedirect(View):
  
  def get(self, request):
    return redirect(f"/accounts/profile/{request.user.profile.pk}")


class UserUpdate(UpdateView):
  model = Profile
  more_fields = ['current_city', 'profile_img']
  template_name = "profile_update.html"

  def get_success_url(self):
    return reverse("profile_detail", kwargs={'pk': self.object.profile.pk})
    
# @login_required
# def profile(self, request):
#   if request.method == 'POST':
#     print('===== its all happenin =====')
#     p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     if p_form.is_valid() and u_form.is_valid():
#       u_form.save()
#       p_form.save()
      
#       return reverse("profile_detail", kwargs={'pk': self.object.profile.pk})
#     else:
#       p_form = ProfileUpdateForm(instance=request.user)
#       u_form = UserUpdateForm(instance=request.user.profile)

#     context={'p_form': p_form, 'u_form': u_form}
#     return render(request, 'accounts/profile/<int:pk>', context)
