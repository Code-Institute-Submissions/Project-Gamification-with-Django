from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    status = models.CharField(max_length=254, default='proposed')
    project_manager = models.CharField(max_length=254, default='')
    proposed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=6, decimal_places = 0, default = 0)
    issues = models.DecimalField(max_digits=2, decimal_places = 0, default = 0)
    image = models.ImageField(upload_to='images')
    
    def get_absolute_url(self):
        return reverse('project_details', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name
        
class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    cost = models.DecimalField(max_digits=3, decimal_places = 0, default = 0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    proposed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('project_details', kwargs={'pk': self.pk})
        
    def __str__(self):
        return self.name