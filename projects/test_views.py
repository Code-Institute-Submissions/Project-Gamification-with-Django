from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import MyProfile
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


class TestViews(TestCase):
    
    def create_project(self, name="Create a Test"):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        return Project.objects.create(name=name,
                                      proposed_by = user)
    
    # def test_get_all_projects_page(self):
    #     user = User.objects.create_user(username='username', password='password')
    #     self.client.login(username='username', password='password')
    #     myprofile = MyProfile.objects.create(owner = user, position="PM", my_wallet=450)
    #     page = self.client.get("/projects", follow=True)
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "projects.html")
        
    # def test_project_details_view(self):
    #     a = self.create_project()
    #     url = reverse('project_details', kwargs={'pk': a.pk})
    #     resp = self.client.get(url, follow=True)
    #     self.assertEqual(reverse('project_details', kwargs={'pk': a.pk}), a.get_absolute_url())
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(a.name, resp.content)
        
        
    
    # def test_get_project_details_page(self):
    #     user = User.objects.create_user(username='username', password='password')
    #     self.client.login(username='username', password='password')
    #     myprofile = MyProfile.objects.create(owner = user, position="PM", my_wallet=450)
    #     project = Project.objects.create(name = 'test', proposed_by = user)
    #     requiredskills = RequiredSkills.objects.create(project = project)
    #     page = self.client.get("/project_details/{0}".format(project.id))
    #     self.assertEqual(page.status_code, 200)
    #     # self.assertTemplateUsed(page, "project_details.html")
    
    
    # def test_get_propose_projects_page(self):
    #     user = User.objects.create_user(username='username', password='password')
    #     self.client.login(username='username', password='password')
    #     myprofile = MyProfile.objects.create(owner = user, position="PM", my_wallet=450)
    #     page = self.client.get("projects/propose_project/", follow=True)
    #     self.assertEqual(page.status_code, 200)
    #     # self.assertTemplateUsed(page, "propose_project.html")
        
    # def test_advance_project_page(self):  
    #     user = User.objects.create_user(username='username', password='password')
    #     self.client.login(username='username', password='password')
    #     myprofile = MyProfile.objects.create(owner = user, position="admin", my_wallet=450)
    #     project = Project(name = 'test', description = 'test', status = 'proposed', proposed_by = user, budget = 55)
    #     project_states = ['state_1', 'state_2']
    #     page = self.client.get("/advance_project/{0}".format(project.id), follow=True)
    #     self.assertEqual(page.status_code, 200)
    
    
    # def test_post_propose_project(self):
    #     user = User.objects.create_user(username='username', password='password')
    #     self.client.login(username='username', password='password')
    #     myprofile = MyProfile.objects.create(owner = user, position="PM", my_wallet=450)
    #     response = self.client.post("/propose_project", {'name' : 'test', 'proposed_by' : user }, follow=True)
    #     project = get_object_or_404(Project, id=1)
    #     self.assertEqual(project.name, 'test')
        
    