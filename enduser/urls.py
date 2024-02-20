from django.urls import path, include
from . import views


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('landing_page/', views.LandingPageView.as_view(), name='landing_page'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]