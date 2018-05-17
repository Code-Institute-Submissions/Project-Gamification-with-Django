from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class MyProfile(models.Model):
    position = models.CharField(max_length=254, default='Coder')
    personality = models.CharField(max_length=254, default='geek')
    image = models.ImageField(upload_to='portraits', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def my_wallet(self):
        my_wallet = 0
        if self.position == "PM":
            my_wallet += 500
        elif self.position == "Coder":
            my_wallet += 100
        else:
            my_wallet += 10
        return my_wallet  
            


    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})
    
    def __str__(self):
        return str(self.owner)
        
        
class Position(models.Model):
    name = models.CharField(max_length=254, default='undefined')
    
    def __str__(self):
        return self.name
    
class Personality(models.Model):
    name = models.CharField(max_length=254, default='undefined')    
    
    def __str__(self):
        return self.name