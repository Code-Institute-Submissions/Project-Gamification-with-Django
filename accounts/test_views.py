from django.test import TestCase
from django.contrib.auth.models import User
from .models import MyProfile

class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "user_login.html")
        
    # def test_get_profile_page(self):
    #     self.user = User.objects.create_user(username='testuser', password='12345')
    #     myprofile = MyProfile.objects.create(owner = self.user, position="test")
    #     # login = self.client.login(username='testuser', password='12345')
    #     page = self.client.get("accounts/profile/{0}".format(self.user.id))
    #     # self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, "projects.html")