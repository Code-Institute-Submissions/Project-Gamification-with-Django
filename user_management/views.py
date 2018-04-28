from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserLoginForm



def index(request):
    return render(request, 'index.html')
    
    
@login_required   
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been successfully log out!")
    return redirect(reverse('index'))

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
             
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Login successfull")   
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Credentials not valid")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            user = authenticate(username=username, password=password, first_name = first_name)
            login(request, user)
            return redirect('index')
            
    else:    
        form = UserRegistrationForm()
        
    context = {'form' : form}
    return render(request, 'registration/register.html', context)
