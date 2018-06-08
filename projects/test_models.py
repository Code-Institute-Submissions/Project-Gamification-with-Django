from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestProjectModel(TestCase):


    def create_project(self, name="Create a Test"):
        user = User.objects.create_user(username='username', password='password')
        return Project.objects.create(name=name,
                                      proposed_by = user)
    
    def test_create_project(self):
        a = self.create_project()
        self.assertTrue(isinstance(a, Project))
    
    
    def test_project_status_defaults_to_proposed(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        project = Project(name="Create a Test", proposed_by = user)
        project.save()
        self.assertEqual(project.name, "Create a Test")
        self.assertEqual(project.status, "proposed")
        
    def test_project_as_a_string(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        project = Project(name="Create a Test", proposed_by = user)
        self.assertEqual("Create a Test", str(project) )