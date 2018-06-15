from django import forms
from .models import Project, Issue, RequiredSkills, ProjectState



######################### NEW PROJECT ########################################## 


class ProposeProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['name','description', 'image']
   
   
######################### NEW ISSUE ############################################  
   
class RaiseIssueForm(forms.ModelForm):
    
    class Meta:
        model = Issue
        fields = ['name','description', 'cost']   
   
######################### REQUIRED SKILLS FOR PROJECT ##########################
   
class RequiredSkillsForm(forms.ModelForm):
    
    class Meta:
        model = RequiredSkills
        exclude = ['project']
   
######################### APPLY FOR A PROJECT TEAM #############################  
   
class CommitSkillForm(forms.Form):
 
    CHOICES=[('html','html'),
             ('css','css'),
             ('js','js'),
             ('db','db'),
             ('python','python')]

    skill = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    
    
######################### ADVANCE PROJECT TO THE NEW STAGE #####################
    
class ChangeStateForm(forms.ModelForm):  
    
    class Meta:
        model = Project
        fields = ['status']
   
   
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   