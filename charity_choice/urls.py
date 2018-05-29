from django.urls import path
from .views import view_backed_projects, support_project, adjust_backed_projects, charities, propose_charity, delete_charity

urlpatterns = [
    path('charities', charities, name="charities"),
    path('propose_charity/', propose_charity, name='propose_charity'),
    path('delete_charity/<int:pk>', delete_charity, name='delete_charity'),
    path('', view_backed_projects, name="view_backed_projects"),
    path('support/<id>', support_project, name="support_project"),
    path('adjust/<id>', adjust_backed_projects, name="adjust_backed_projects")
    ]