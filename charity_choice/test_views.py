from django.test import TestCase
from .models import *
from .forms import *
from accounts.models import MyProfile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

class TestViews(TestCase):
    
    
    def test_get_home_page(self):
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
        page = self.client.get("/charity_choice/propose_charity/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "propose_charity.html")

    def test_post_charity_details(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        myprofile = MyProfile.objects.create(owner = self.user, my_wallet=450, position='admin')
        form = ProposeCharityForm()
        response = self.client.post("/charities/propose_charity/", {'name' : 'Test', 'description' : "Test" })
        charity = get_object_or_404(Charity, pk=1)
        # self.assertNotContains(response, 'something went wrong' ,200) 
        # self.assertEqual(myprofile.position, "Coder")        
        
        
        
        
        
#     def test_get_profile_page(self):
        # self.user = User.objects.create_user(username='testuser', password='12345')
        # myprofile = MyProfile.objects.create(owner = self.user, position="test")
        # login = self.client.login(username='testuser', password='12345')
#         page = self.client.get("/accounts/profile/{0}".format(self.user.id))
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, "profile.html")
        
#     def test_post_profile_details(self):
#         self.user = User.objects.create_user(username='username', password='password')
#         self.client.login(username='username', password='password')
#         myprofile = MyProfile.objects.create(owner = self.user, my_wallet=450)
#         response = self.client.post("/accounts/profile/{0}".format(self.user.id), data = {'position' : 'Coder'}, follow=True)
#         self.assertNotContains(response, 'something went wrong' ,200) 
#         self.assertEqual(myprofile.position, "Coder")
     
        
#     def test_issue_fixed_page(self):
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         myprofile = MyProfile.objects.create(owner = self.user, position="test")
#         login = self.client.login(username='testuser', password='12345')    
#         project = Project.objects.create(name = 'test', proposed_by = self.user)
#         issue = Issue.objects.create(name = "Test", description = "Test", cost = 1, project = project, assigned_to = self.user)
#         page = self.client.get("/accounts/profile/{0}".format(self.user.id))
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, "profile.html")
        
        
#     def test_get_gamification_test(self):
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         myprofile = MyProfile.objects.create(owner = self.user, position="test")
#         login = self.client.login(username='testuser', password='12345')
#         page = self.client.get("/accounts/profile/gamification_test/{0}".format(self.user.id))
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, "gamification_test.html")
        
#     def test_post_gamification_test(self):
#         self.user = User.objects.create_user(username='username', password='password')
#         self.client.login(username='username', password='password')
#         myprofile = MyProfile.objects.create(owner = self.user, position="PM", my_wallet=450)
#         answers_list = []
#         response = self.client.post("/profile/gamification_test/{0}".format(self.user.id), answers_list.extend(('answer_1', 'answer_1')), follow=True)
#         self.assertEqual(answers_list , ['answer_1', 'answer_1'])    
        