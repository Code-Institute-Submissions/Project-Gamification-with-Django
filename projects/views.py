from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project, Issue, RequiredSkills, Team, CommitSkill, ProjectState, ProjectMessage
from accounts.models import MyProfile
from .forms import ProposeProjectForm, RaiseIssueForm, RequiredSkillsForm, CommitSkillForm, ChangeStateForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
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
    project_log = ProjectMessage.objects.filter(project = project).order_by('-message_date')
    
    issue_counter = len(issues)
    
    context = {'project': project, 
                'issues': issues, 
                'issue_counter': issue_counter, 
                'requiredskills' : requiredskills,
                'project_team': project_team,
                'skill_coverage': skill_coverage,
                'project_log': project_log }
   
    
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
                                         message = "Issue {0} raised by {1}".format(new_issue.name, new_issue.assigned_to)
                                         ).save
               
               
           project.budget = project.budget - new_issue.cost
           if project.budget < 0:
               project.status = "On Hold"
               ProjectMessage.objects.create(
                   project = project,
                   message = "Project {0} placed on hold.".format(project.name)
                   ).save()
           project.save()
      
               
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
        
        return HttpResponseRedirect('/')
        
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
                   message = "Project {0} proposed by {1}".format(new_project.name, new_project.proposed_by)
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
    
    my_profile = MyProfile.objects.get(owner=project.proposed_by)
    
    form = ChangeStateForm(request.POST, instance = project)
    
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
        
            ProjectMessage.objects.create(
                       project = project,
                       message = "Project {0} advanced to stage {1}".format(project.name, project.status)
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
                
            
        return HttpResponseRedirect('/')
        
    
    return render (request, 'complete_project.html', {'project': project, 'team_members' : team_members, 'prize' : prize, 'project_team' : project_team })
    


def assign_issue(request, pk):
    
    user = request.user
    issue = get_object_or_404(Issue, id=pk)
    issue.assigned_to = request.user
    issue.save()
    
    ProjectMessage.objects.create(
                   project = issue.project,
                   message = "Issue {0} assigned to {1}".format(issue.name, issue.assigned_to)
                   ).save()
    
        
    return HttpResponseRedirect('/') 
        
    