from django.urls import path, include
from .views import all_projects, project_details, propose_project, delete_project, join_team, leave_team, reject_candidate, advance_project, complete_project, assign_issue

urlpatterns = [
    path('', all_projects, name="projects"),                                        ## dashboard      
    
    path('project_details/<int:pk>', project_details, name='project_details'),      ## project details
    
    path('propose_project/', propose_project, name='propose_project'),              ## add new project
    
    path('project_details/delete_project/<int:pk>', delete_project,                 ## delete project that's on hold
                                                    name='delete_project'),
    path('project_details/reject_candidate/<int:pk>', reject_candidate,             ## remove from proposed team
                                                      name='reject_candidate'),
    path('project_details/<int:pk>/join', join_team, name='join_team'),             ## apply for project team
    path('project_details/<int:pk>/leave', leave_team, name='leave_team'),
    path('project_details/<int:pk>/advance_project', advance_project,               ## move project to the next stage
                                                     name='advance_project'),
    path('project_details/<int:pk>/complete_project', complete_project,             ## finish project, reward team    
                                                      name='complete_project'),
    path('project_details/<int:pk>/assign_issue/<int:ik>', assign_issue,            ## apply to fix an issue
                                                           name='assign_issue')
    ]