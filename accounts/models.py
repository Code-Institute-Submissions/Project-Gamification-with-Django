from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class MyProfile(models.Model):
    position = models.CharField(max_length=254, default='rookie')
    personality = models.CharField(max_length=254, default='programmer')
    image = models.ImageField(upload_to='portraits')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.position
        
        
class Position(models.Model):
    name = models.CharField(max_length=254, default='undefined')
    
    def __str__(self):
        return self.name
    
class Personality(models.Model):
    name = models.CharField(max_length=254, default='undefined')    
    
    def __str__(self):
        return self.name