from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Game


def game_detail(request, year, month, day, game_slug):
    game = get_object_or_404(Game,
                                slug=game_slug,
                                release_date__year=year,
                                release_date__month=month,
                                release_date__day=day)
    return render(request, 'games/game_detail.html', {'game': game})

class GameListView(ListView):
    model = Game
    