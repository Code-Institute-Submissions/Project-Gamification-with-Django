from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project, Issue, Skill, RequiredSkills, Team, CommitSkill, ProjectState
from accounts.models import MyProfile
from .forms import ProposeProjectForm, RaiseIssueForm, RequiredSkillsForm, CommitSkillForm, ChangeStateForm, AssignIssueForm
from django.urls import reverse
from django.http import HttpResponseRedirect
import collections



def all_projects(request):
    projects = Project.objects.all()

    status_list = []
    for element in projects:
        status = element.status
        status_list.append(status)
        
    count_them = collections.Counter( status_list )
    
    context = {"projects": projects, 
                "count_them": count_them  }
    
   
    return render(request, "projects.html", context)

 
def project_details(request, pk):
    project = Project.objects.get(id=pk)
    issues = Issue.objects.filter(project=project)
    requiredskills = get_object_or_404(RequiredSkills, project=project)
    project_team = Team.objects.filter(projects = project)
    skill_coverage = CommitSkill.objects.filter(project = project)
    
    issue_counter = len(issues)
    
    context = {'project': project, 
                'issues': issues, 
                'issue_counter': issue_counter, 
                'requiredskills' : requiredskills,
                'project_team': project_team,
                'skill_coverage': skill_coverage}
   
    
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
           
           Issue.objects.create(
               name = name,
               description = description,
               cost = cost,
               project = project,
               assigned_to = assigned_to
               ).save()
      
               
        requiredskillsform = RequiredSkillsForm(request.POST, instance = requiredskills)
        
        if requiredskillsform.is_valid():
            requiredskills = requiredskillsform.save()
            
        return redirect(reverse('project_details', kwargs={'pk': pk }))    
          


    return render(request, 'project_details.html', context, { 'form': form, 'requiredskillsform': requiredskillsform } )   


@login_required
def propose_project(request):
    
    my_profile = get_object_or_404(MyProfile, owner=request.user)
    
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
               
            
     
 

           return redirect(reverse('projects'))
       
    else:
        form = ProposeProjectForm()
        
    return render (request, 'propose_project.html', {'form': form })    
    
    
def delete_project(request, pk):
    
    if request.method == 'DELETE':
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        
    return HttpResponseRedirect('/')
    
    
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
    
    form = ChangeStateForm(request.POST, instance = project)
    
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            
            
            return redirect(reverse('project_details', kwargs={'pk': pk }))
        
    return render (request, 'advance_project.html', {'form': form, 'project': project, 'project_states' : project_states })    
    
    
## BUILD     

def complete_project(request, pk):
    
    project = Project.objects.get(pk=pk)
    project_team = Team.objects.filter(projects = project)
    
    team_members = 0
    for element in project_team:
        team_members += 1

    prize = project.budget_left() / team_members
    
    if request.method == 'POST':
        
        for element in project_team:
            user = element.current_user
            winners = MyProfile.objects.filter(owner=user)
            for element in winners:
                element.my_wallet += prize
                element.save()
        
        project.delete()        
                
            
        return HttpResponseRedirect('/')
        
    
    return render (request, 'complete_project.html', {'project': project, 'team_members' : team_members, 'prize' : prize, 'project_team' : project_team })
    
   
## RESOLVE_ISSUE VIEW 


def assign_issue(request, pk):
    
    issue = Issue.objects.get(id=pk)
    user = request.user
    form = AssignIssueForm(request.POST)
    
    if request.method == 'POST':

        issue = get_object_or_404(Issue, id=pk)
        issue.assigned_to = request.user
        issue.save()
        return HttpResponseRedirect('/')
        
    return render (request, 'assign_issue.html',  {'issue' : issue, 'user' : user} ) 
        
    