from django.db import models
from django.core.url.resolvers import reverse


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    status = models.CharField(max_length=254, default='proposed')
    project_manager = models.CharField(max_length=254, default='')
    budget = models.DecimalField(max_digits=6, decimal_places = 0, default = 0)
    issues = models.DecimalField(max_digits=2, decimal_places = 0, default = 0)
    image = models.ImageField(upload_to='images')
    
    def get_absolute_url(self):
        return reverse('project')
    
    def __str__(self):
        return self.name
        
    