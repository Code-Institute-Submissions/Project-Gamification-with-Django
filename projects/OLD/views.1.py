from django.shortcuts import render
from .models import Project


def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})
    
def project_details(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project_details.html', {'project': project})
