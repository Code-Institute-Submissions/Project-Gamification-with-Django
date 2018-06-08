from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestMyProfiletModel(TestCase):

    def create_myprofile(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(position='PM', personality='socializer', owner = user)
        return MyProfile.objects.create(position=position,
                                        personality = personality,
                                        owner = owner)
    
    def test_create_myprofile(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(position='PM', personality='socializer', owner = user)
        self.assertTrue(isinstance(myprofile , MyProfile))
    
    
    def test_myprofile_position_defaults_to_coder(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(personality='socializer', owner = user)
        myprofile.save()
        self.assertEqual(myprofile.position, "Coder")
        self.assertEqual(myprofile.personality, "socializer")
        
    # def test_project_as_a_string(self):
    #     user = User.objects.create_user(username='username', password='password')
    #     self.client.login(username='username', password='password')
    #     project = Project(name="Create a Test", proposed_by = user)
    #     self.assertEqual("Create a Test", str(project) )