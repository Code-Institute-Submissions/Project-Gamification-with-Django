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
    


def view_donations(request):
    """A view that renders the cart contents page"""
    return render(request, "view_donations.html")
    

def delete_charity(request, pk):

    if request.method == 'DELETE':
        charity = get_object_or_404(Charity, pk=pk)
        charity.delete()
            
        return redirect(reverse('charities'))    

    
def add_to_donations(request, id):
    
    quantity=1
    
    chosen_donations = request.session.get('chosen_donations', {})
    chosen_donations[id] = chosen_donations.get(id, quantity)
    
    request.session['chosen_donations'] = chosen_donations
    return redirect(reverse('charities'))
    

def adjust_donations(request, id):
    
    chosen_donations = request.session.get('chosen_donations', {})
    
    chosen_donations.pop(id)
        
    request.session['chosen_donations'] = chosen_donations
    return redirect(reverse('charities'))