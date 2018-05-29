from django import forms
from .models import Charity

class ProposeCharityForm(forms.ModelForm):
    
    class Meta:
        model = Charity
        fields = ['name','description', 'image']