from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from enduser.models import CustomUser



class Post(models.Model):
    content =  models.TextField()
    image =  models.ImageField(upload_to='feeds/post_images', blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(CustomUser, related_name='likes',blank=True)
    tagged_users = models.ManyToManyField(CustomUser, related_name='tagged_users',blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.content[:10]

    def get_absolute_url(self):
        return reverse("post:post-detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
