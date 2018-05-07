from django.urls import path, include
from .views import all_projects, project_details, propose_project, delete_project

urlpatterns = [
    path('', all_projects, name="projects"),
    path('project_details/<int:pk>', project_details, name='project_details'),
    path('propose_project/', propose_project, name='propose_project'),
    path('delete_project/<int:pk>', delete_project, name='delete_project'),
    ]