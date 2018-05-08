from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, MyDetailsForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import MyProfile
from projects.models import Project, Issue


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
def profile(request):
    """A view that displays the profile page of a logged in user"""
    user = request.user
    issues = Issue.objects.filter(proposed_by=request.user)
    projects = Project.objects.filter(proposed_by=request.user)
    my_profile = MyProfile.objects.filter(owner=request.user)
    return render(request, 'profile.html', {'user': user, 'projects': projects, 'issues': issues, 'my_profile': my_profile })



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
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()
        login_form = UserLoginForm()

    args = {'user_form': user_form, 'login_form': login_form, 'next': request.GET.get('next', '')}
    return render(request, 'user_login.html', args)

@login_required
def my_details(request):
    
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

           return redirect(reverse('profile'))
       
    else:
       form = MyDetailsForm()
        
    return render (request, 'my_details.html', {'form': form })    
    
    
    
    
    
    
    