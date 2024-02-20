from django.db import models
from enduser.models import Organizer, Gamer, CustomUser
from games.models import Game

class Tournament(models.Model):
    class Status(models.TextChoices):
        COMPLETED = "Completed", 'COMPLETED'
        IN_PROGRESS = "In_progress", 'IN_PROGRESS'
        PENDING = "Pending", 'PENDING'
        CANCELLED = "Cancelled", 'CANCELLED'
        POSTPONED = "Postponed", 'POSTPONED'
        SUSPENDED = "Suspended", 'SUSPENDED'

    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)

    tournament_status = models.CharField(max_length=100, choices=Status.choices)
    # ForeignKey indicates a many-to-one relationship.
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, null=True, related_name='tournament_organizer')
    description = models.TextField()
    partner = models.CharField(max_length=200, blank=True)
    registration_deadline = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    location = models.CharField(max_length=200,null=True, blank=True)
    prize_pool = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    max_players = models.PositiveIntegerField(default=0)
    rules = models.TextField(blank=True)

    players = models.ForeignKey(Gamer, related_name='tournament_players', on_delete=models.SET_NULL, null=True, blank=True)
    runner_up = models.ForeignKey(Gamer, related_name='tournament_runner_up', on_delete=models.SET_NULL, null=True, blank=True)
    winner = models.ForeignKey(Gamer, related_name='tournament_winner', on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='games/thumbnails', null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

