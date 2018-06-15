from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



######################### USER DETAILS ######################################### 


class MyProfile(models.Model):
    position = models.CharField(max_length=254, default='Coder', blank=True)
    personality = models.CharField(max_length=254, default='', blank=True)
    image = models.ImageField(upload_to='portraits', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    my_wallet = models.DecimalField(max_digits=6, decimal_places = 0, default = 0)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"   


    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})
    
    def __str__(self):
        return str(self.owner)

######################### COMPANY POSITIONS ####################################
  
        
class Position(models.Model):
    name = models.CharField(max_length=254, default='undefined')
    
    class Meta:
        verbose_name = "Company Position"
        verbose_name_plural = "Company Positions" 
    
    def __str__(self):
        return self.name
    
######################### GAMIFICATION PERSONALITY TYPES #######################
    
    
class Personality(models.Model):
    name = models.CharField(max_length=254, default='undefined')    
    
    class Meta:
        verbose_name = "Personality Type"
        verbose_name_plural = "Personality Types" 
        
    def __str__(self):
        return self.name
        
        