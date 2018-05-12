from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Issue
from .forms import ProposeProjectForm, RaiseIssueForm
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
    
    issue_counter = len(issues)
    
    context = {'project': project, 
                'issues': issues, 
                'issue_counter': issue_counter }
   
    
    if request.method == 'GET':
        return render(request, 'project_details.html', context )
        
    elif request.method == 'POST':
        
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
           

    return render(request, 'project_details.html', context)   


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
           
           Project.objects.create(
               name = name,
               description = description,
               project_manager = project_manager,
               budget = budget,
               image = image,
               proposed_by = proposed_by
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
    