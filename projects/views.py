from django.shortcuts import render
from .models import Project


def all_projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})
    
