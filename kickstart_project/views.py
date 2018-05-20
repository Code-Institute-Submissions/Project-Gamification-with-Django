from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_backed_projects(request):
    return render(request, "kickstart_project.html")
    
def support_project(request, id):
    quantity=int(request.POST.get('quantity'))
    
    chosen_projects = request.session.get('chosen_projects', {})
    chosen_projects[id] = chosen_projects.get(id, quantity)
    
    request.session['chosen_projects'] = chosen_projects
    return redirect(reverse('login_page'))
    

def adjust_backed_projects(request, id):
    
    quantity = int(request.POST.get('quantity'))
    chosen_projects = request.session.get('chosen_projects', {})
    
    if quantity > 0:
        chosen_projects[id] = quantity
    else:
        chosen_projects.pop(id)
        
    request.session['chosen_projects'] = chosen_projects
    return redirect(reverse('view_backed_projects'))