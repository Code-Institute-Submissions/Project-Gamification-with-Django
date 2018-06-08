from django.test import TestCase
from .forms import *


class TestDonationForm(TestCase):
    
    def test_successful_donation_form(self):
        form = DonationForm({'donor': 'Tester'})
        self.assertTrue(form.is_valid())  
    
    def test_blank_donation_entry(self):
        form = DonationForm({'donor': ''})
        self.assertFalse(form.is_valid())    
        
        
class TestMakeDonationForm(TestCase):
        
    def test_blank_field_make_donation_form(self):
        form = MakeDonationForm({
            'credit_card_number': '4242424242424242',  
            'cvv': '111',  
            'expiry_month': '', 
            'expiry_year': '2022',
            'stripe_id': '',
            })
        self.assertFalse(form.is_valid())        