from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import *


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2
    
    
class MyDetailsForm(forms.ModelForm):
    
    class Meta:
        model = MyProfile
        fields = ['position','personality','image']
        
        
        
class PersonalityForm(forms.Form):

    CHOICES_1=[('answer_1','Run your own tavern?'),
             ('answer_2','Have a sword twice as powerful as any other in the game?'),
             ('answer_3','Three charges of a spell that allows you control other players, against their will?'),
             ('answer_4','Know more secrets than any other players?')]
             
    question_1=forms.CharField(label="In a game, would you rather:", widget=forms.RadioSelect(choices=CHOICES_1))
    
    
    CHOICES_2=[('answer_1','A great storyline.'),
             ('answer_2','Solving a riddle no one else has gotten.'),
             ('answer_3','Being the most Feared person in the game.'),
             ('answer_4','Making your own maps of the world and selling them.')]
             
    question_2=forms.CharField(label="In a game, you enjoy the most:", widget=forms.RadioSelect(choices=CHOICES_2))
    
    
    CHOICES_3=[('answer_1','You get a big group of players to help you defeat it.'),
             ('answer_2','Find the way to kill monsters by yourself as no one did before.'),
             ('answer_3','You attack him before he attacks you.'),
             ('answer_4','Hide somewhere you know the monster cannot follow you.')]
             
    question_3=forms.CharField(label="In a game, you have encountered big monster:", widget=forms.RadioSelect(choices=CHOICES_3))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        