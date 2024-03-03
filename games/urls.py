from django.urls import path, include
from . import views

app_name = 'games'

urlpatterns = [
    path('list/', views.GameListView.as_view(), name='game-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:game>/', views.game_detail, name='game_detail'),
]