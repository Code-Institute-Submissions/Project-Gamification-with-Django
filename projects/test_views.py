from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    def test_get_projects_page(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        # self.assertTemplateUsed(page, "projects.html")