from django.test import TestCase
from .models import *
from charity_choice.models import Charity
        
class TestDonationModel(TestCase):        
    
    def create_donation(self):
        donation = Donation.objects.create(donor='Test')
        return Donation.objects.create(donor=donor)
    
    def test_create_donation(self):
        donation = Donation.objects.create(donor='Test') 
        self.assertTrue(isinstance(donation , Donation))
        
    def test_charity_name_defaults_to_donor(self):
        donation = Donation.objects.create() 
        donation.save()
        self.assertEqual(donation.donor, "Donor")
        
    def test_donation_as_a_string(self):
        donation = Donation.objects.create(donor='Test')
        self.assertEqual("Test", str(donation))
        
        
class TestDonationLineItemModel(TestCase):        
    
    def create_donationlineitem(self):
        donation = Donation.objects.create(donor='Test')
        charity = Charity.objects.create(name='Test', description="Test")
        donationlineitem = DonationLineItem.objects.create(donation = donation, charity = charity, quantity = 1)
        self.assertTrue(isinstance(donationlineitem , DonationLineItem))
    
    def test_quantity_defaults_to_1(self):
        donation = Donation.objects.create(donor='Test')
        charity = Charity.objects.create(name='Test', description="Test")
        donationlineitem = DonationLineItem.objects.create(donation = donation, charity = charity)
        self.assertEqual(donationlineitem.quantity, 1)
        
    def test_donationlineitem_as_a_string(self):
        donation = Donation.objects.create(donor='Test')
        charity = Charity.objects.create(name='Test', description="Test")
        donationlineitem = DonationLineItem.objects.create(donation = donation, charity = charity)
        self.assertEqual("Test", str(donationlineitem))