from django.db import models
from django.urls import reverse
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,  unique_for_date='release_date')
    genre = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    published_by = models.CharField(max_length=200, null=True, blank=True)
    developed_by = models.CharField(max_length=200, null=True, blank=True)
    platform = models.CharField(max_length=50, null=True, blank=True)
    publisher_website = models.URLField(max_length=200, null=True, blank=True)

    release_date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='games/thumbnails', null=True, blank=True)
    game_cover = models.ImageField(upload_to= 'games/covers', null=True, blank=True)
    trailer_link = models.URLField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("games:game_detail", args=[self.release_date.year,
                                                    self.release_date.month,
                                                    self.release_date.day,
                                                    self.slug])
    
    

