from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    model = Tournament
    fields = ['name', 'game','description','organizer','start_time', 'registration_deadline']