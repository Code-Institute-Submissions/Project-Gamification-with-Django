from django.test import TestCase
from .models import *
from .forms import *
from accounts.models import MyProfile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

class TestViews(TestCase):
    
    
    
    def test_get_charity_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        myprofile = MyProfile.objects.create(owner = self.user, position="test")
        login = self.client.login(username='testuser', password='12345')
        page = self.client.get("/charity_choice/charities")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "charities.html")
        
    def test_get_view_donations_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        myprofile = MyProfile.objects.create(owner = self.user, position="test")
        login = self.client.login(username='testuser', password='12345')
        page = self.client.get("/charity_choice/view_donations")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_donations.html")
    

    
        
