from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import uuid
from django.utils import timezone



class Profile(models.Model):
    """"Profile model to handle database logic"""
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    profile_picture = models.URLField(
        null=True, blank=True, default="https://icons8.com/icon/sLFSAGKrdDPq/test-account")
    bio = models.TextField(max_length=300, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        """Returns a string representation of model instance"""
        return f"{self.user.username}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
