from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    # prevent a clash with reverse acessor names in Django models
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    

class Profile(models.Model):
    user = models.OneToOneField(User, null=False, primary_key=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    # profile_pic = models.ImageField(default='static/default_profilepic/default.jpg', blank=True, upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
    
    
    