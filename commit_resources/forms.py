from django import forms
from .models import Donation

class DonateForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2017, 2036)]
    

class SupportProjectForm(forms.Form):
    class Meta:
        model = Donation
        fields = ('full_name', 'position')