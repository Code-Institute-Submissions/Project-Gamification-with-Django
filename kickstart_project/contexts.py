from django.shortcuts import get_object_or_404
from projects.models import Project


def support_project(request):
    
    chosen_projects = request.session.get('chosen_projects', {})
    
    backed_projects = []
    total = 0
    project_count = 0
    for id, quantity in chosen_projects.items():
        project = get_object_or_404(Project, pk=id)
        total += quantity * project.budget
        project_count += quantity
        backed_projects.append({'id':id, 'quantity': quantity, 'project' : project})
        
    return { 'backed_projects': backed_projects, 'total': total, 'project_count' : project_count }     
        
    
    
    