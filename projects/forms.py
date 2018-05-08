from django import forms
from .models import Project

class ProposeProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['name','description','project_manager','budget']
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   