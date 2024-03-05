from django.db import models
from enduser.models import CustomUser, Organizer, Gamer

class Space(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    admin = models.ManyToManyField(Organizer, related_name="space_admin")
    members = models.ManyToManyField(CustomUser, blank=True, related_name="space_members", )
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    space_logo = models.ImageField(upload_to='space/logo', null=True, blank=True)
    space_banner = models.ImageField(upload_to= 'space/banner', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
