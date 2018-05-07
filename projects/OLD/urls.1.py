from django.urls import path, include
from .views import all_projects, project_details

urlpatterns = [
    path('', all_projects, name="projects"),
    path('project_details/<int:pk>', project_details, name='project_details'),
    ]