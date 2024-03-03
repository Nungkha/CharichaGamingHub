from django.urls import path
from . import views

app_name = 'tournament'

urlpatterns = [
    path('', views.TournamentListView.as_view(), name='tournament-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:tournament>/', views.tournament_detail, name='tournament_detail'),
    path('create/', views.TournamentCreateView.as_view(), name='create-tournament'),

]