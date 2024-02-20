# Generated by Django 5.0.2 on 2024-02-19 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enduser', '0001_initial'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tournament_status', models.CharField(choices=[('Completed', 'COMPLETED'), ('In_progress', 'IN_PROGRESS'), ('Pending', 'PENDING'), ('Cancelled', 'CANCELLED'), ('Postponed', 'POSTPONED'), ('Suspended', 'SUSPENDED')], max_length=100)),
                ('description', models.TextField()),
                ('partner', models.CharField(blank=True, max_length=200)),
                ('registration_deadline', models.DateTimeField(blank=True, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('prize_pool', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('entry_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('max_players', models.PositiveIntegerField(default=0)),
                ('rules', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='games/thumbnails')),
                ('is_active', models.BooleanField(default=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.game')),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament_organizer', to='enduser.organizer')),
                ('players', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament_players', to='enduser.gamer')),
                ('runner_up', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament_runner_up', to='enduser.gamer')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament_winner', to='enduser.gamer')),
            ],
        ),
    ]
