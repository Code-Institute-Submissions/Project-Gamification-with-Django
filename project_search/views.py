from django.shortcuts import render
from django.views import generic
from projects.models import Project
from accounts.models import MyProfile
import collections

# Create your views here.

def find_project(request):
    projects = Project.objects.filter(name__icontains=request.GET['query'])
    profiles = MyProfile.objects.all()

    status_list = []
    for element in projects:
        status = element.status
        status_list.append(status)
        
    count_them = collections.Counter( status_list )
    
    context = {"projects": projects, 
                "count_them": count_them,
                "profiles": profiles}
    
   
    return render(request, "projects.html", context)