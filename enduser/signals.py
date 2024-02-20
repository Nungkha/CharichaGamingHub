from django.db.models.signals import post_save
from .models import CustomUser, Profile
from django.dispatch import receiver



# when new user is created
# Profile object of new user is automatically created using signals

@receiver(post_save, sender=CustomUser)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance, user_type=instance.user_type)
        profile.save()
    else:
        # If an existing CustomUser is updated, update the associated Profile
        instance.profile.user_type = instance.user_type
        instance.profile.save()







