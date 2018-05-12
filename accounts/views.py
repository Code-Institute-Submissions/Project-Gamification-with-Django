from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, MyDetailsForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import MyProfile, Personality, Position
from projects.models import Project, Issue
from django.utils.text import slugify


# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))



@login_required
def profile(request, user):
    
    user = request.user
    issues = Issue.objects.filter(proposed_by=request.user)
    projects = Project.objects.filter(proposed_by=request.user)
    
    project_count = 0
    for element in projects:
        project_count += 1
        
    issue_count = 0
    for element in issues:
        issue_count +=1
    

    personalities = Personality.objects.all()
    positions = Position.objects.all()
    my_profile = get_object_or_404(MyProfile, owner=request.user)
    
    
    context = {'user': user, 'projects': projects, 'issues': issues, 
                'my_profile': my_profile, 'personalities': personalities, 
                'positions': positions, 'project_count': project_count, 
                'issue_count': issue_count, }
    
    if request.method == 'GET':
 
        return render(request, 'profile.html', context)
    
    if request.method == 'POST':
       my_profile = get_object_or_404(MyProfile, owner=request.user)
       form = MyDetailsForm(request.POST, request.FILES, instance=my_profile)
       
       if form.is_valid():
           my_profile = form.save()
              
       else:
           form = MyDetailsForm()       

    return render(request, 'profile.html', { 'form': form } , context)
   



def user_login(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password are incorrect")
                
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            
            
            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                
                MyProfile.objects.create(
                position = "guest",
                personality = "guest",
                owner = request.user
                ).save()
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()
        login_form = UserLoginForm()

    context = {'user_form': user_form, 
                'login_form': login_form, 
                'next': request.GET.get('next', '')}
                
    return render(request, 'user_login.html', context)
    

@login_required
def my_details(request, owner):
    
    personalities = Personality.objects.all()
    positions = Position.objects.all()
    if request.method == 'POST':
       
       form = MyDetailsForm(request.POST, request.FILES)
       
       if form.is_valid():
           position = form.cleaned_data['position']
           personality = form.cleaned_data['personality']
           image = form.cleaned_data['image']
           owner = request.user
           
           MyProfile.objects.create(
               position = position,
               personality = personality,
               image = image,
               owner = owner
               ).save()

           return HttpResponseRedirect('/')
       
    else:
       form = MyDetailsForm()
        
    return render (request, 'my_details.html', {'form': form, 'personalities': personalities, 'positions': positions })   
           

    
    
    
    
    