from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import MyProfile
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone


class TestViews(TestCase):
    
    def create_project(self, name="Create a Test"):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        return Project.objects.create(name=name,
                                      proposed_by = user)
    
    def test_get_all_projects_page(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(owner = user, position="PM", my_wallet=450)
        page = self.client.get("/projects", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "projects.html")
        

    def test_get_propose_projects_page(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(owner = user, position="PM", my_wallet=450)
        current_time = timezone.now()
        page = self.client.get("/projects/propose_project/", follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "propose_project.html")
        
    def test_advance_project_page(self):  
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(owner = user, position="admin", my_wallet=450)
        project = Project(name="Create a Test", proposed_by = user)
        project.save()
        project = get_object_or_404(Project, pk=1)
        page = self.client.get("/projects/project_details/1/advance_project/", follow=True)
    

        
    