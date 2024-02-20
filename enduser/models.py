from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

""" base user """

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class User_Types(models.TextChoices):
        GAMER = "Gamer", 'GAMER'
        ORGANIZER = "Organizer", 'ORGANIZER'


    email = models.EmailField(_('Email address'), unique=True)
    username = models.CharField(max_length = 250, unique=True)
    user_type = models.CharField(max_length = 20 , choices = User_Types.choices)
    joined_at = models.DateField(default = timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']

    class Meta:
        ordering = ['-joined_at']
        indexes = [
            models.Index(fields=['-email','username']),
        ]

    def __str__(self):
        return self.username
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.user_type = self.base_user_type
    #         return super().save(*args, **kwargs)

        

""" GAMER """


class GamerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(user_type=CustomUser.User_Types.GAMER.value)


class Gamer(CustomUser):
    gamer = GamerManager()

    class Meta:
        proxy = True

    def game(self):
        return 'Hello Gamers'
    





""" ORGANIZER """


class OrganizerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(user_type=CustomUser.User_Types.ORGANIZER.value)


class Organizer(CustomUser):
    
    organizer = OrganizerManager()

    class Meta:
        proxy = True

    def game(self):
        return 'Hello Gamers'


"""  Profile """


class Profile(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_type = models.CharField(max_length = 20)
    bio = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default = timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='profile_image') 
    cover_photo = models.ImageField(default='cover.jpg', upload_to= 'cover_images')

    def __str__(self):
        return f"{self.user.username} Profile"



