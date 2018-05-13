from django import forms
from .models import Project, Issue, RequiredSkills

class ProposeProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['name','description','project_manager','budget', 'image']
   
   
class RaiseIssueForm(forms.ModelForm):
    
    class Meta:
        model = Issue
        fields = ['name','description', 'cost']   
   
   
class RequiredSkillsForm(forms.ModelForm):
    
    class Meta:
        model = RequiredSkills
        exclude = ['project']
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   