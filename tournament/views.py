from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from .models import Tournament
from .forms import  TournamentForm
from django.contrib.auth.mixins import LoginRequiredMixin

# class TournamentView(TemplateView):
#     template_name = 'tournament/tournament.html'

class TournamentListView(LoginRequiredMixin, ListView):
    template_name = 'tournament/tournament.html'
    model = Tournament

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user_tournaments = Tournament.objects.filter(organizer=self.request.user)
        other_tournaments = Tournament.objects.exclude(organizer=self.request.user)

        context['user_tournaments'] = user_tournaments
        context['other_tournaments'] = other_tournaments

        return context


class TournamentCreateView(CreateView):
    model = Tournament
    # fields = ['name', 'game','thumbnail','description','prize_pool']
    form_class = TournamentForm
    template_name = 'tournament/tournament_create.html'
    success_url = '../'


    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)



# class TournamentUpdateView(UpdateView):
#     model = Tournament
#     fields = ['name', 'game', 'organizer','description','prize_pool']
#     template_name = 'tournament/tournament_update.html'
#     success_url = 'list-tournament'



def tournament_detail(request, year, month, day, tournament):
    tournament = get_object_or_404(Tournament,
                                slug=tournament,
                                start_time__year=year,
                                start_time__month=month,
                                start_time__day=day)
    return render(request, 'tournament/tournament_detail.html', {'tournament': tournament})