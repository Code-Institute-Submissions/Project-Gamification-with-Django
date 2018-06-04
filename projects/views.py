from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from accounts.models import MyProfile
from .forms import ProposeProjectForm, RaiseIssueForm, RequiredSkillsForm, CommitSkillForm, ChangeStateForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
import collections


@login_required
def all_projects(request):
    projects = Project.objects.all()
    profiles = MyProfile.objects.all()
    my_profile = get_object_or_404(MyProfile, owner=request.user)

    status_list = []
    for element in projects:
        status = element.status
        status_list.append(status)
        
    count_them = collections.Counter( status_list )
    
    context = {"projects": projects, 
                "count_them": count_them,
                "profiles": profiles,
                "my_profile": my_profile,}
    
   
    return render(request, "projects.html", context)

@login_required
def project_details(request, pk):
    project = Project.objects.get(id=pk)
    issues = Issue.objects.filter(project=project)
    profiles = MyProfile.objects.all()
    requiredskills = get_object_or_404(RequiredSkills, project=project)
    project_team = Team.objects.filter(projects = project)
    skill_coverage = CommitSkill.objects.filter(project = project)
    project_log = ProjectMessage.objects.filter(project = project).order_by('-message_date')
    my_profile = get_object_or_404(MyProfile, owner=request.user)
    issue_counter = len(issues)
    
    achievers = 0
    explorers = 0
    socializers = 0
    killers = 0
    for element in project_team:
        team_profiles = MyProfile.objects.filter(owner=element.current_user)
        for row in team_profiles:
            if row.personality == "achiever":
                achievers += 1
            elif row.personality == "explorer":
                explorers += 1   
            elif row.personality == "socializer":
                socializers += 1       
            elif row.personality == "killer":
                killers += 1  
                
                
    efficiency_ratio = socializers * (-2) + explorers * 1 + killers * 2 + achievers * 3
    innovation_ratio = socializers * (-2) + explorers * 3 + killers * 2 + achievers * 1
    teamwork_ratio =  socializers * 2 + explorers * (-2) + killers * (-2) + achievers * (-2)
    
    if efficiency_ratio > 5:
        statement_1 = get_object_or_404(GamificationAdvice, name="efficiency++")  
    elif 0 < efficiency_ratio <= 5:
        statement_1 = get_object_or_404(GamificationAdvice, name="efficiency+") 
    elif -5 <= efficiency_ratio < 0:
        statement_1 = get_object_or_404(GamificationAdvice, name="efficiency-")
    elif efficiency_ratio < -5:
        statement_1 = get_object_or_404(GamificationAdvice, name="efficiency--")    
    else:
        statement_1 = get_object_or_404(GamificationAdvice, name="efficiency0")
        
    if innovation_ratio > 5:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation++")  
    elif 0 < innovation_ratio <= 5:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation+") 
    elif -5 <= innovation_ratio < 0:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation-")
    elif innovation_ratio < -5:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation--")    
    else:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation0")    
        
    if teamwork_ratio > 5:
        statement_3 = get_object_or_404(GamificationAdvice, name="teamwork++")  
    elif 0 < teamwork_ratio <= 5:
        statement_3 = get_object_or_404(GamificationAdvice, name="teamwork+") 
    elif -5 <= teamwork_ratio < 0:
        statement_3 = get_object_or_404(GamificationAdvice, name="teamwork-")
    elif teamwork_ratio < -5:
        statement_3 = get_object_or_404(GamificationAdvice, name="teamwork--")    
    else:
        statement_3 = get_object_or_404(GamificationAdvice, name="teamwork0")    
    
    
    project_ratios = [efficiency_ratio, innovation_ratio, teamwork_ratio]
    
    if max(project_ratios) == efficiency_ratio and efficiency_ratio != 0:
        team_type = "Robot Factory"
    elif  max(project_ratios) == innovation_ratio and innovation_ratio != 0:  
        team_type = "Research Lab"
    elif max(project_ratios) == teamwork_ratio and teamwork_ratio != 0:  
        team_type = "Think tank"
    else:
        team_type = "Equilibrium"
        

    context = {'project': project, 
                'issues': issues, 
                'profiles': profiles,
                'my_profile': my_profile,
                'issue_counter': issue_counter, 
                'requiredskills' : requiredskills,
                'project_team': project_team,
                'skill_coverage': skill_coverage,
                'project_log': project_log,
                'achievers': achievers,
                'explorers': explorers,
                'socializers': socializers,
                'killers': killers,
                'team_profiles' : team_profiles,
                'efficiency_ratio' : efficiency_ratio,
                'innovation_ratio' : innovation_ratio,
                'teamwork_ratio' : teamwork_ratio,
                'team_type' : team_type, 
                'statement_1': statement_1,
                'statement_2': statement_2,
                'statement_3': statement_3
     }
    
    if request.method == 'GET':
        return render(request, 'project_details.html', context )
        
    elif request.method == 'POST':
        requiredskills = get_object_or_404(RequiredSkills, project=project)
        
        form = RaiseIssueForm(request.POST)
       
        if form.is_valid():
           name = form.cleaned_data['name']
           description = form.cleaned_data['description']
           cost = form.cleaned_data['cost']
           project = project
           assigned_to = request.user
           
           new_issue = Issue.objects.create(
                                           name = name,
                                           description = description,
                                           cost = cost,
                                           project = project,
                                           assigned_to = assigned_to)
           new_issue.save()
           
           ProjectMessage.objects.create(project = project,
                                         message = 'Issue "{0}" raised by pm {1}'.format(new_issue.name, new_issue.assigned_to)
                                         ).save
               
               
           project.budget = project.budget - new_issue.cost
           if project.budget < 0:
               project.status = "hold"
               ProjectMessage.objects.create(
                   project = project,
                   message = 'Project "{0}" placed on hold.'.format(project.name)
                   ).save()
           project.save()
           
           
        else:
            form = RaiseIssueForm(request.POST)
               
               
               
        requiredskillsform = RequiredSkillsForm(request.POST, instance = requiredskills)
        
        if requiredskillsform.is_valid():
            requiredskills = requiredskillsform.save()
            
        return redirect(reverse('project_details', kwargs={'pk': pk }))    
        
        
        
          


    return render(request, 'project_details.html', context, { 'form': form, 'requiredskillsform': requiredskillsform } )   


@login_required
def propose_project(request):
    
    my_profile = get_object_or_404(MyProfile, owner=request.user)
    current_time = timezone.now()
    
    if my_profile.my_wallet < 450:
        
        return redirect(reverse('projects'))
        
    else: 
        
        if request.method == 'POST':
    
           form = ProposeProjectForm(request.POST, request.FILES)
           
           if form.is_valid():
               name = form.cleaned_data['name']
               description = form.cleaned_data['description']
               budget = 450
               image = form.cleaned_data['image']
               proposed_by = request.user
               
               new_project = Project.objects.create(
                                                   name = name,
                                                   description = description,
                                                   budget = budget,
                                                   image = image,
                                                   proposed_by = proposed_by
                                                   )
               new_project.save()
               
               
               my_profile.my_wallet = my_profile.my_wallet - 450
               my_profile.save()
               
               RequiredSkills.objects.create(
                    project = new_project
                   ).save()
                   
               ProjectMessage.objects.create(
                   project = new_project,
                   message = 'Project "{0}" proposed by user {1}'.format(new_project.name, new_project.proposed_by)
                   ).save()       
                   
                   
               return redirect(reverse('projects'))
               
       
        else:
            form = ProposeProjectForm()
        
    return render (request, 'propose_project.html', {'form': form })    
    
    
def delete_project(request, pk):
    ## change post to delete for charities
    # if request.method == 'POST':
    project = get_object_or_404(Project, pk=pk)
    project.delete()
        
    return redirect(reverse('projects'))
    
    
def join_team(request, pk):
    project = Project.objects.get(pk=pk)
    Team.join_team(request.user, project)
    requiredskills = get_object_or_404(RequiredSkills, project=project)
    
    form = CommitSkillForm(request.POST)
    
    if request.method == 'POST':
        
        if form.is_valid():
            skill = form.cleaned_data['skill']
            CommitSkill.objects.create(
                    project = project,
                    user = request.user,
                    skill = skill
                    ).save()
      
        return redirect(reverse('project_details', kwargs={'pk': pk }))
       
    
    return render (request, 'join_team.html', {'form': form, 'requiredskills' : requiredskills })
    
def leave_team(request, pk):
    project = Project.objects.get(pk=pk)
    commitskill = get_object_or_404(CommitSkill, project=project, user=request.user)
    commitskill.delete() 
    Team.leave_team(request.user, project)
    
    return redirect(reverse('project_details', kwargs={'pk': pk }))
    
  

def reject_candidate(request, pk):
    
    if request.method == 'DELETE':
        commitskill = get_object_or_404(CommitSkill, pk=pk)
        user = commitskill.user
        project = commitskill.project
        commitskill.delete()   
        Team.leave_team(user, project)
   
    return redirect(reverse('project_details', kwargs={'pk': pk }))    
    

def advance_project(request, pk):
    
    project = Project.objects.get(pk=pk)
    project_states = ProjectState.objects.all()
    
    my_profile = MyProfile.objects.get(owner=project.proposed_by)
    
    form = ChangeStateForm(request.POST, instance = project)
    
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
        
            ProjectMessage.objects.create(
                       project = project,
                       message = 'Project "{0}" advanced to stage "{1}"'.format(project.name, project.status)
                       ).save()    
            
            
            return redirect(reverse('project_details', kwargs={'pk': pk }))
        
    return render (request, 'advance_project.html', {'form': form, 'project': project, 'project_states' : project_states, 'my_profile' : my_profile })    
    
    
## BUILD     

def complete_project(request, pk):
    
    project = Project.objects.get(pk=pk)
    project_team = Team.objects.filter(projects = project)
    project_manager = MyProfile.objects.get(owner=project.proposed_by)
    
    team_members = 0
    for element in project_team:
        team_members += 1

    prize = project.budget / team_members
    
    if request.method == 'POST':
        
        project_manager.my_wallet = project_manager.my_wallet + 450
        project_manager.save()
        
        for element in project_team:
            user = element.current_user
            winners = MyProfile.objects.filter(owner=user)
            for element in winners:
                element.my_wallet += prize
                element.save()
                
                
        
        project.delete()        
                
            
        return redirect(reverse('projects'))
        
    
    return render (request, 'complete_project.html', {'project': project, 'team_members' : team_members, 'prize' : prize, 'project_team' : project_team })
    


def assign_issue(request, pk, ik):
    
    project = Project.objects.get(pk=pk)
    user = request.user
    issue = get_object_or_404(Issue, id=ik)
    issue.assigned_to = request.user
    issue.save()
    
    ProjectMessage.objects.create(
                   project = issue.project,
                   message = 'Issue "{0}" assigned to user {1}'.format(issue.name, issue.assigned_to)
                   ).save()
    

    return redirect(reverse('project_details', kwargs={'pk': pk }))   
        
    