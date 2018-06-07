from django.test import TestCase
from .forms import ProposeProjectForm



class TestProposeProjectForm(TestCase):
    
    def test_cant_create_a_project_with_just_a_name(self):
        form = ProposeProjectForm({'name': 'Create Tests'})
        self.assertFalse(form.is_valid())

    def test_project_form_for_missing_name(self):
        form = ProposeProjectForm({'name': ''})
        self.assertFalse(form.is_valid())