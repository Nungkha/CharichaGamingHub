from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import ProfileUpdateForm, UserUpdateForm
from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Profile

# LoginRequiredMixin is used to view Template only if User is authenticated/logged in
class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'enduser/home.html'
    extra_content = {'section': 'dashboard'}
    login_url = 'login'

class LandingPageView(TemplateView):
    template_name = 'enduser/landing_page.html'
    # extra_content = {'section': 'dashboard'}
    login_url = 'login'

    

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'enduser/profile/profile.html', {'profile': profile})


def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'enduser/profile/update_profile.html', {'form': form})