from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # bio field is now non-nullable and has a default value
    bio = models.TextField(default="This user hasn't provided a bio yet.", blank=True)
    
    # profile_picture field remains optional (nullable)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    
    # followers field with updated related_name to avoid clashes
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following_users', blank=True)

    def __str__(self):
        return self.username
