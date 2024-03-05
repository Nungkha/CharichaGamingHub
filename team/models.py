from django.db import models
from enduser.models import CustomUser

class Team(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    members = models.ManyToManyField(CustomUser, blank=True, related_name="team_members",)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    team_logo = models.ImageField(upload_to='team/logo', null=True, blank=True)
    team_banner = models.ImageField(upload_to= 'team/banner', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
