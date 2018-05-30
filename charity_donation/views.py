from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import DonationForm, MakeDonationForm
from .models import DonationLineItem
from charity_choice.models import Charity
from django.conf import settings
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def charity_donation(request):
    if request.method=="POST":
        donation_form = DonationForm(request.POST)
        make_donation_form = MakeDonationForm(request.POST)
        
        if donation_form.is_valid() and make_donation_form.is_valid():
            donation = donation_form.save(commit=False)
            donation.save()
            
            chosen_donations = request.session.get('chosen_donations', {})
            total = 0
            for id, quantity in chosen_donations.items():
                charity = get_object_or_404(Charity, pk=id)
                total += quantity * charity.donation
                donation_line_item = DonationLineItem(
                    donation = donation,
                    charity = charity
                    )
                donation_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = make_donation_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('charities'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(make_donation_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        donation_form = DonationForm()
        make_donation_form = MakeDonationForm()
            
    return render(request, "charity_donation.html", {'donation_form': donation_form, 'make_donation_form': make_donation_form, 'publishable': settings.STRIPE_PUBLISHABLE })    