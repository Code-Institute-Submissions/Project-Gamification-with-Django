from django import forms
from .models import Project, Issue, RequiredSkills, ProjectState

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
   
   
class CommitSkillForm(forms.Form):
 
    CHOICES=[('python','python'),
             ('html','html'),
             ('css','css'),
             ('js','js'),
             ('db','db')]

    skill = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    
    
class ChangeStateForm(forms.ModelForm):  
    
    class Meta:
        model = Project
        fields = ['status']
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   