from django import forms
from .models import Charity


######################### ADD CHARITY FORM #####################################
    

class ProposeCharityForm(forms.ModelForm):
    
    class Meta:
        model = Charity
        fields = ['name','description', 'image']