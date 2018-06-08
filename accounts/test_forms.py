from django.test import TestCase
from .forms import *


class TestUserRegistrationForm(TestCase):
    
    def test_can_create_an_user_with_just_a_name(self):
        form = UserRegistrationForm({'name': 'Create Tests'})
        self.assertFalse(form.is_valid())

    def test_user_form_for_missing_name(self):
        form = UserRegistrationForm({'name': ''})
        self.assertFalse(form.is_valid())
 
class TestMyProfileForm(TestCase):        
        
    def test_should_create_an_myprofile_with_just_a_position(self):
        form = MyDetailsForm({'position': 'Test'})
        self.assertTrue(form.is_valid())
        
    def test_blank_myprofile_form_should_work(self):
        form = MyDetailsForm({'position': '', 'image': ''})
        self.assertTrue(form.is_valid())
    
class TestPersonalityForm(TestCase):     
    
    def test_shouldnt_save_personality_test_with_missing_answer(self):
        form = PersonalityForm({'question_1':''})
        self.assertFalse(form.is_valid())
        