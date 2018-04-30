from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    project_manager = models.CharField(max_length=254, default='')
    budget = models.DecimalField(max_digits=6, decimal_places = 0)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name