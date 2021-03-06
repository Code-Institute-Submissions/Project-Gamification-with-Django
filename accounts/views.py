from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from .forms import *
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import *
from projects.models import Project, Issue, TeamMember, ProjectMessage
from projects.views import all_projects





######################### LOGIN & REGISTRATION PAGE ############################


def login_page(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)                                ## login handling
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
                    return redirect(reverse('login_page'))
            else:
                login_form.add_error(None, "Your username or password are incorrect")
                
        user_form = UserRegistrationForm(request.POST)                          ## registration handling
        if user_form.is_valid():
            user_form.save()
            
            
            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                
                MyProfile.objects.create(                                       ## create default user details    
                position = "guest",
                personality = "",
                my_wallet = 0,
                owner = request.user
                ).save()
                return redirect('projects/')

            else:
                messages.error(request, "unable to log you in at this time!")
        else:
            messages.error(request, "Invalid Credentials")
                
    else:
        user_form = UserRegistrationForm()
        login_form = UserLoginForm()

    context = {'user_form': user_form, 
                'login_form': login_form, 
                'next': request.GET.get('next', 'projects/' )}
                
    return render(request, 'user_login.html', context)


######################### LOGOUT PAGE ##########################################


@login_required
def logout(request):
    
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('login_page'))
    
    


######################### USERS PROFILE PAGE ###################################


@login_required
def profile(request, pk):
    
    user = request.user
    issues = Issue.objects.filter(assigned_to=request.user)
    projects = Project.objects.filter(proposed_by=request.user)
    try:                                                                        ## handling empty joined_projects
        joined_teams = get_object_or_404(TeamMember, 
                                         current_user = request.user)
        joined_projects = joined_teams.projects.all()
    except:
        joined_projects = []
    
    
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
                'issue_count': issue_count, 'joined_projects' : joined_projects }
    
    if request.method == 'GET':
 
        return render(request, 'profile.html', context)
    
## USER ADDS HIS OWN DETAILS  

    if request.method == 'POST':                        
       my_profile = get_object_or_404(MyProfile, owner=request.user)
       form = MyDetailsForm(request.POST, request.FILES, instance=my_profile)
       
       if form.is_valid():                                                      ## Amount of credits depends on user's position
           my_profile = form.save(commit=False)
           if my_profile.position == "PM" and my_profile.my_wallet == 0:
            my_profile.my_wallet = 500  
           elif my_profile.position == "Coder" and my_profile.my_wallet == 0:  
            my_profile.my_wallet = 100  
           else:
            my_profile.my_wallet = my_profile.my_wallet    
            
           my_profile.save()
            
           return redirect(reverse('profile', kwargs={'pk': pk }))          
    else:
        form = MyDetailsForm()       

    return render(request, 'profile.html', { 'form': form } , context)
   

######################### USERS FIXES BUG ######################################
           
           
@login_required
def issue_fixed(request, pk):
    
    issue = get_object_or_404(Issue, id=pk)
    # project = get_object_or_404(Project, name = issue.project)
    my_profile = get_object_or_404(MyProfile, owner=request.user)
    
    my_profile.my_wallet = my_profile.my_wallet + issue.cost                    ## reward
    my_profile.save()
    issue.delete()
    
    ProjectMessage.objects.create(
                   project = issue.project,
                   message = 'Issue "{0}" fixed by user {1}'.format(issue.name, issue.assigned_to)
                   ).save()
    
  
    return redirect(reverse('profile', kwargs={'pk': pk }))
    
    
######################### GAMIFICATION PERSONALITY TEST ########################


@login_required    
def gamification_test(request, pk):
    
    my_profile = get_object_or_404(MyProfile, owner=request.user)
    form = PersonalityForm(request.POST)
    
    if request.method == 'POST':
        first = request.POST.get('question_1')
        second = request.POST.get('question_2')
        third = request.POST.get('question_3')
        fourth = request.POST.get('question_4')
        fifth = request.POST.get('question_5')
        sixth = request.POST.get('question_6')
        answers_list = [first, second, third, fourth, fifth, sixth]
        score = 0
        for element in answers_list:                                            ## score counter
            if element == "answer_1":
                score += 1
            elif element == "answer_2": 
                score += 3
            elif element == "answer_3":
                score += 4
            elif element == "answer_4":
                score += 2
        if  score <= 11:                    
            my_profile.personality = 'socializer'                               ## assign users personality
        elif 11 < score <= 15:
            my_profile.personality = 'explorer'
        elif 15 < score <= 20:
            my_profile.personality = 'achiever'
        else:    
            my_profile.personality = 'killer'
            
        my_profile.save()    
        
      
        return redirect(reverse('profile', kwargs={'pk': pk }))
    
    return render(request, 'gamification_test.html', {'form': form})