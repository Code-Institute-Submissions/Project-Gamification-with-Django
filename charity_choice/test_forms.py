from django.test import TestCase
from .forms import *


class TestProposeCharityForm(TestCase):        
        
    def test_shouldnt_create_charity_with_just_a_name(self):
        form = ProposeCharityForm({'name': 'Test'})
        self.assertFalse(form.is_valid())
        
    def test_blank_myprofile_form_shouldnt_work(self):
        form = ProposeCharityForm({'name': '', 'position': '', 'image': ''})
        self.assertFalse(form.is_valid())