from django.test import TestCase
from .forms import UserRegistrationForm


class TestUserRegistrationForm(TestCase):
    
    def test_can_create_an_user_with_just_a_name(self):
        form = UserRegistrationForm({'name': 'Create Tests'})
        self.assertFalse(form.is_valid())

    def test_form_for_missing_name(self):
        form = UserRegistrationForm({'name': ''})
        self.assertFalse(form.is_valid())