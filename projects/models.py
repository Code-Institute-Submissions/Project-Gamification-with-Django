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
    image = models.ImageField(upload_to='images')
    
    
    def budget_left(self):
        issues = Issue.objects.filter(project=self)
        total_cost_amount = 0
        for issue in issues:
            total_cost_amount += issue.cost
        
        return self.budget - total_cost_amount    
    
    
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
        
     
class Skill(models.Model):
    name = models.CharField(max_length=254)
    logo = models.ImageField(upload_to='logos', blank=True)
    
    def __str__(self):
        return self.name
        
        
class RequiredSkills(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    python = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    html = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    js = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    css = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    mongodb = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    mysql = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    
    def __str__(self):
        return str(self.project)    
        
        
        
        
class Team(models.Model):
    projects = models.ManyToManyField(Project)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    @classmethod
    def join_team(cls, current_user, new_project):
        team, created = cls.objects.get_or_create(
            current_user=current_user
        )
        team.projects.add(new_project)
        
    @classmethod
    def leave_team(cls, current_user, new_project):
        team, created = cls.objects.get_or_create(
            current_user=current_user
        )
        team.projects.remove(new_project)    
            
        