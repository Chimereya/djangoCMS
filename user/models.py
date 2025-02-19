from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(default='static/default_profilepic/default.jpg', blank=True, upload_to='profile_pics')
    website_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    
     
class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    
    
    

    
    
    