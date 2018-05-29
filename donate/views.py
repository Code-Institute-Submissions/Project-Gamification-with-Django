from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DonateForm, SupportProjectForm
from django.conf import settings

# Create your views here.


@login_required()
def finalize_donation(request):
    if request.method=="POST":
        donate_form = DonateForm(request.POST)
        support_project_form = SupportProjectForm(request.POST)
        
        if donate_form.is_valid() and support_project_form.is_valid():
            donation = donate_form.save(commit=False)
            donation.date = timezone.now()
            donation.save()
            
            chosen_donations = request.session.get('chosen_donations', {})
            total = 0
            for id, quantity in chosen_donations.items():
                project = get_object_or_404(Project, pk=id)
                total += quantity * project.budget
                supported_project = SupportedProject(
                    donation = donation,
                    project = project,
                    quantity = quantity
                    )
                supported_project.save()
        else:
            print(support_project_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        donate_form = DonateForm()
        support_project_form = SupportProjectForm()
            
        return render(request, "xxxxx.html", {'payment_form': payment_form, 'support_project_form': support_project_form })    