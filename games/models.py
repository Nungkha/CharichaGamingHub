from django.db import models



class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    published_by = models.CharField(max_length=200, null=True, blank=True)
    developed_by = models.CharField(max_length=200, null=True, blank=True)
    platform = models.CharField(max_length=50, null=True, blank=True)
    publisher_website = models.URLField(max_length=200, null=True, blank=True)

    release_date = models.DateTimeField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='games/thumbnails', null=True, blank=True)
    trailer_link = models.URLField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name
    

