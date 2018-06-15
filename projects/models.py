from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


######################### PROJECT DETAILS ######################################


class Project(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(blank=False)
    status = models.CharField(max_length=254, default='proposed')
    proposed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=6, decimal_places = 0, default = 0)
    image = models.ImageField(upload_to='images') 
    
    class Meta:
        verbose_name = "Project Summary"
        verbose_name_plural = "Projects Summary"    
    
    def __str__(self):
        return self.name
        
        
######################### PROJECT STATE ########################################  
        
        
class ProjectState(models.Model):
    name = models.CharField(max_length=254, default='proposed')
    
    class Meta:
        verbose_name = "Project State"
        verbose_name_plural = "Projects States" 
      
    def __str__(self):
        return self.name    
        
        
######################### ISSUE DETAILS ########################################  
        
        
class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(blank=False)
    cost = models.DecimalField(max_digits=3, decimal_places = 0, default = 0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = "Bugs & Issues"
        verbose_name_plural = "Bugs & Issues" 
        
    def __str__(self):
        return "{0}-{1}".format(self.project.name, self.name)       
        

######################### REQUIRED SKILLSET FOR PROJECT ########################
        
        
class RequiredSkills(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    python = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    html = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    js = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    css = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)
    db = models.DecimalField(max_digits=1, decimal_places = 0, default = 0)

    class Meta:
        verbose_name = "Required Skillset"
        verbose_name_plural = "Required Skillsets" 
        
        
    def __str__(self):
        return str(self.project)    

######################### TEAM MEMBERSHIP ######################################        
      
        
class TeamMember(models.Model):
    projects = models.ManyToManyField(Project)                                  ## many-to-many relationship
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members" 
    
    @classmethod
    def join_team(cls, current_user, new_project):                              ## join team
        teammember, created = cls.objects.get_or_create(
            current_user=current_user
        )
        teammember.projects.add(new_project)
        
        
    @classmethod
    def leave_team(cls, current_user, new_project):                             ## leave team
        teammember, created = cls.objects.get_or_create(
            current_user=current_user
        )
        teammember.projects.remove(new_project)    
        
    def __str__(self):
        return str(self.current_user)       
        
        
######################### APPLY FOR PROJECT TEAM ###############################     


class CommitSkill(models.Model):  
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=254, default='html')
    
    class Meta:
        verbose_name = "Skill Coverage"
        verbose_name_plural = "Skills Coverage" 
        
        
    def __str__(self):
        return "{0}-{1}".format(self.project.name, self.user.username)   
        
        
######################### PROJECT LOG MESSAGES #################################
        
        
class ProjectMessage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.project)
    
    
######################### GAMIFICATION ADVICE ##################################    
    
    
class GamificationAdvice(models.Model):
    name =  models.CharField(max_length=254, default='advice')
    advice = models.TextField(blank=False)
    
    def __str__(self):
        return str(self.name)
