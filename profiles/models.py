from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import uuid
from django.utils import timezone



class Profile(models.Model):
    """"Profile model to handle database logic"""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_bhadqa'
    )
    bio = models.TextField(max_length=300, null=True, blank=True)
    

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        """Returns a string representation of model instance"""
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
