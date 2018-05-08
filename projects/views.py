from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Issue
from .forms import ProposeProjectForm, RaiseIssueForm
from django.urls import reverse
from django.http import HttpResponseRedirect



def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

 
def project_details(request, pk):
    project = Project.objects.get(id=pk)
    issues = Issue.objects.filter(project=project)
    return render(request, 'project_details.html', {'project': project, 'issues': issues })


@login_required
def propose_project(request):
    
    if request.method == 'POST':
       
       form = ProposeProjectForm(request.POST)
       
       if form.is_valid():
           name = form.cleaned_data['name']
           description = form.cleaned_data['description']
           project_manager = form.cleaned_data['project_manager']
           budget = form.cleaned_data['budget']
           proposed_by = request.user
           
           Project.objects.create(
               name = name,
               description = description,
               project_manager = project_manager,
               budget = budget,
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
    

@login_required
def raise_issue(request, pk):
    
    project = Project.objects.get(id=pk)
    
    if request.method == 'POST':
       
       form = RaiseIssueForm(request.POST)
       
       if form.is_valid():
           name = form.cleaned_data['name']
           description = form.cleaned_data['description']
           project = project
           proposed_by = request.user
           
           Issue.objects.create(
               name = name,
               description = description,
               project = project,
               proposed_by = proposed_by
               ).save()

           return HttpResponseRedirect('/')
       
    else:
        form = RaiseIssueForm()
        
    return render (request, 'raise_issue.html', {'form': form })        