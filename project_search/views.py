from django.shortcuts import render
from projects.models import Project

# Create your views here.

def find_project(request):
    projects = Project.objects.filter(name__icontains=request.GET['query'])
    return render(request, "projects.html", {"projects":projects})