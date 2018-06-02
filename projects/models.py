from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    status = models.CharField(max_length=254, default='proposed')
    proposed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=6, decimal_places = 0, default = 0)
    image = models.ImageField(upload_to='images')
    
    class Meta:
        verbose_name = "Project Summary"
        verbose_name_plural = "Projects Summary"    

    
    def get_absolute_url(self):
        return reverse('project_details', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name
        
   
        
        
class ProjectState(models.Model):
    name = models.CharField(max_length=254, default='proposed')
      
    def __str__(self):
        return self.name    
        
        

        
class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    cost = models.DecimalField(max_digits=3, decimal_places = 0, default = 0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('project_details', kwargs={'pk': self.pk})
        
    def __str__(self):
        return self.name        
        


        
class RequiredSkills(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    python = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    html = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    js = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    css = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    db = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)

    
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
            
    def __str__(self):
        return str(self.current_user)       
        

class CommitSkill(models.Model):  
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=254, default='')
    
    
    def __str__(self):
        return str(self.project)
        

        
class ProjectMessage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.TextField()
    message_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.project)
    
    
class ProjectMessageSummary(ProjectMessage):
    class Meta:
        proxy = True
        verbose_name = "Project Message Summary"
        verbose_name_plural = "Project Messages Summary"    
    
    
    
## IDEA
# def __str__(self):
#         return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)