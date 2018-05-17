from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Issue, Skill, RequiredSkills, Team, CommitSkill, ProjectState
from .forms import ProposeProjectForm, RaiseIssueForm, RequiredSkillsForm, CommitSkillForm, ChangeStateForm
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
           proposed_by = request.user
           
           Issue.objects.create(
               name = name,
               description = description,
               cost = cost,
               project = project,
               proposed_by = proposed_by
               ).save()
      
               
        requiredskillsform = RequiredSkillsForm(request.POST, instance = requiredskills)
        
        if requiredskillsform.is_valid():
            requiredskills = requiredskillsform.save()
            
        return redirect(reverse('project_details', kwargs={'pk': pk }))    
          


    return render(request, 'project_details.html', context, { 'form': form, 'requiredskillsform': requiredskillsform } )   


@login_required
def propose_project(request):
    
    if request.method == 'POST':
       
       form = ProposeProjectForm(request.POST, request.FILES)
       
       if form.is_valid():
           name = form.cleaned_data['name']
           description = form.cleaned_data['description']
           project_manager = form.cleaned_data['project_manager']
           budget = form.cleaned_data['budget']
           image = form.cleaned_data['image']
           proposed_by = request.user
           
           new_project = Project.objects.create(
                                               name = name,
                                               description = description,
                                               project_manager = project_manager,
                                               budget = budget,
                                               image = image,
                                               proposed_by = proposed_by
                                               )
           new_project.save()
           
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
    
    if request.method == 'POST':
        pass
    
    return render (request, 'complete_project.html', {'project': project, 'team_members' : team_members })