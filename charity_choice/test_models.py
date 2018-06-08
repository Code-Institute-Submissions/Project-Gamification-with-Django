from django.test import TestCase
from .models import *
        
class TestCharityModel(TestCase):        
    
    def create_charity(self):
        charity = Charity.objects.create(name='Test', description="Test")
        return Charity.objects.create(name=name, description=description)
    
    def test_create_charity(self):
        charity = Charity.objects.create(name='Test', description="Test") 
        self.assertTrue(isinstance(charity , Charity))
        
    def test_charity_name_defaults_to_charity(self):
        charity = Charity.objects.create(description="Test") 
        charity.save()
        self.assertEqual(charity.name, "Charity")
        self.assertEqual(charity.description, "Test")    
        
    def test_charity_as_a_string(self):
        charity = Charity.objects.create(name='Test', description="Test")  
        self.assertEqual("Test", str(charity))
        
        
