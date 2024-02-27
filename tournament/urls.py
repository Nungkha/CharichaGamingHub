from django.urls import path
from . import views

app_name = 'tournament'

urlpatterns = [
    path('', views.TournamentView.as_view(), name='tournament'),
    path('list/', views.TournamentListView.as_view(), name='list-tournament'),
    path('create/', views.TournamentCreateView.as_view(), name='create-tournament'),

]