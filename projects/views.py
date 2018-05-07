from django.shortcuts import render, redirect
from .models import Project
from .forms import ProposeProjectForm
from django.urls import reverse


def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})
    
def project_details(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project_details.html', {'project': project})

def propose_project(request):
    
    if request.method == 'POST':
       
       form = ProposeProjectForm(request.POST)
       
       if form.is_valid():
           name = form.cleaned_data['name']
           description = form.cleaned_data['description']
           project_manager = form.cleaned_data['project_manager']
           budget = form.cleaned_data['budget']
           
           Project.objects.create(
               name = name,
               description = description,
               project_manager = project_manager,
               budget = budget
               ).save()

           return redirect(reverse('projects'))
       
    else:
        form = ProposeProjectForm()
        
    return render (request, 'propose_project.html', {'form': form })    