from django.shortcuts import get_object_or_404
from charity_choice.models import Charity


def add_to_donations(request):
    
    chosen_donations = request.session.get('chosen_donations', {})
    
    backed_charities = []
    total = 0
    charity_count = 0
    for id in chosen_donations.items():
        project = get_object_or_404(Project, pk=id)
        total += charity.donation
        charity_count += 1
        backed_charities.append({'id':id, 'charity' : charity})
        
    return { 'backed_charities': backed_charities, 'total': total, 'charity_count' : charity_count }     
        
    
    
    