from django.urls import path, include
from .views import all_projects, project_details, propose_project, delete_project, join_team, leave_team, reject_candidate

urlpatterns = [
    path('', all_projects, name="projects"),
    path('project_details/<int:pk>', project_details, name='project_details'),
    path('propose_project/', propose_project, name='propose_project'),
    path('delete_project/<int:pk>', delete_project, name='delete_project'),
    path('project_details/reject_candidate/<int:pk>', reject_candidate, name='reject_candidate'),
    path('project_details/<int:pk>/join', join_team, name='join_team'),
    path('project_details/<int:pk>/leave', leave_team, name='leave_team')
    ]