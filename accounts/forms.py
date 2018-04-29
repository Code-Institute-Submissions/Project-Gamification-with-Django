from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
    
    
#####

class UserRegistrationForm(UserCreationForm):
    position = forms.CharField(required = False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'position', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email
        
    def clean_position(self):
        position = self.cleaned_data.get('position')
        return position    

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2
# class UserRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(required = False)
#     last_name = forms.CharField(required = False)
#     email = forms.EmailField(required = False)
#     position = forms.CharField(required = False)
#     skillset = forms.CharField(required = False)
#     current_projects = forms.CharField(required = False)
#     current_issues = forms.CharField(required = False)
#     wallet = forms.IntegerField(required = False)
    
#     class Meta:
#         model = User
#         fields = ('username','first_name', 'last_name', 'email', 'position', 'skillset', 'current_projects', 'current_issues', 'wallet', 'password1', 'password2')        

#     def save(self,commit = True):   
#         user = super(UserRegistrationForm, self).save(commit = False)
#         user.email = self.cleaned_data['email']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.position = self.cleaned_data['position']
#         user.skillset = self.cleaned_data['skillset']
#         user.current_projects = self.cleaned_data['current_projects']
#         user.current_issues = self.cleaned_data['current_issues']
#         user.wallet = self.cleaned_data['wallet']


#         if commit:
#             user.save()

#         return user    
    
#####    
class UserLoginForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)