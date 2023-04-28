import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_folder(sender, instance, created, **kwargs):
    if created:
        # create a new folder with the username of the new user
        username = instance.username
        folder_path = os.path.join(settings.MEDIA_ROOT, username)
        os.mkdir(folder_path)
