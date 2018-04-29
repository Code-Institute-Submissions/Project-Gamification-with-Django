from django.urls import path, include
from .views import all_projects

urlpatterns = [
    path('', all_projects, name="projects"),
    ]