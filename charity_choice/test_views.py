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
        
    def test_get_propose_charity_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        myprofile = MyProfile.objects.create(owner = self.user, position="test")
        login = self.client.login(username='testuser', password='12345')
        charity = Charity.objects.create(name='Test', description="Test")
        charity = get_object_or_404(Charity, pk=1)
        page = self.client.get("/charity_choice/propose_charity/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "propose_charity.html")

    # def test_post_charity_details(self):
    #     self.user = User.objects.create_user(username='username', password='password')
    #     # self.client.login(username='username', password='password')
    #     self.client.force_login(self.user)
    #     myprofile = MyProfile.objects.create(owner = self.user, my_wallet=450, position='admin')
    #     image = /static/img/ai.jpg
    #     response = self.client.post("/propose_charity", {'name' : 'Test', 'description' : 'Test', 'donation' : 5 })
    #     charity = get_object_or_404(Charity, pk=1)
    # #     # self.assertNotContains(response, 'something went wrong' ,200) 
    # #     # self.assertEqual(myprofile.position, "Coder")        
        
        
    def test_get_view_donations_page(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        myprofile = MyProfile.objects.create(owner = self.user, position="test")
        login = self.client.login(username='testuser', password='12345')
        page = self.client.get("/charity_choice/view_donations")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_donations.html")
    
    # def test_add_to_donations_page(self):
    #     self.user = User.objects.create_user(username='testuser', password='12345')
    #     myprofile = MyProfile.objects.create(owner = self.user, position="admin")
    #     login = self.client.login(username='testuser', password='12345')
    #     charity = Charity.objects.create(name='Test', description="Test")
    #     page = self.client.get("/charity_choice/delete_charity/{0}".format(charity.id), follow=True)
    #     # self.assertEqual(page.status_code, 200)
    #     # # self.assertTemplateUsed(page, "charities.html")
    
        
