from django import forms
from .models import Project, Issue

class ProposeProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['name','description','project_manager','budget', 'image']
   
   
class RaiseIssueForm(forms.ModelForm):
    
    class Meta:
        model = Issue
        fields = ['name','description', 'cost']   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   