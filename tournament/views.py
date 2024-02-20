from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from .models import Tournament
from .forms import  TournamentForm


class TournamentView(TemplateView):
    template_name = 'tournament/tournament.html'

class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournament/tournament_list.html'
    # context_object_name = 'articles'


class TournamentCreateView(CreateView):
    model = Tournament
    fields = ['name', 'game', 'organizer','description','prize_pool']
    template_name = 'tournament/tournament_create.html'
    success_url = '../list'



class TournamentUpdateView(UpdateView):
    model = Tournament
    fields = ['name', 'game', 'organizer','description','prize_pool']
    template_name = 'tournament/tournament_update.html'
    success_url = 'list-tournament'