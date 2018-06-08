from django.test import TestCase
from .models import *
from accounts.models import MyProfile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

class TestViews(TestCase):
    
    
    def test_get_project_search_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        myprofile = MyProfile.objects.create(owner = self.user, position="test")
        login = self.client.login(username='testuser', password='12345')
        page = self.client.get("/find_project/?query=asd")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "projects.html")
        

