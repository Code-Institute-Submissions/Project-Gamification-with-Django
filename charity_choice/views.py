from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from .forms import ProposeCharityForm
from .models import Charity
from accounts.models import MyProfile
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


# Create your views here.

def charities(request):
    
    charities = Charity.objects.all()
    my_profile = get_object_or_404(MyProfile, owner=request.user)
    
    context = {"charities": charities,
                "my_profile": my_profile}
    
    return render(request, "charities.html", context)

    

@login_required
def propose_charity(request):
    

    if request.method == 'POST':

        form = ProposeCharityForm(request.POST, request.FILES)
       
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            donation = 5
            image = form.cleaned_data['image']
           
            new_charity = Charity.objects.create(
                                                name = name,
                                                description = description,
                                                donation = donation,
                                                image = image,
                                                )
            new_charity.save()

               
            return redirect(reverse('charities'))
           
   
    else:
        form = ProposeCharityForm()
        
    return render (request, 'propose_charity.html', {'form': form })    
    

def delete_charity(request, pk):

    if request.method == 'DELETE':
        charity = get_object_or_404(Charity, pk=pk)
        charity.delete()
            
        return redirect(reverse('charities'))    















def view_backed_projects(request):
    return render(request, "charity_choice.html")
    
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