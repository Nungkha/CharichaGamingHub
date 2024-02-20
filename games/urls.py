from django.urls import path, include
from . import views


urlpatterns = [
    path('list/', views.GameListView.as_view(), name='game-list'),

]