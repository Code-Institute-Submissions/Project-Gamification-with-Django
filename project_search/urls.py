from django.urls import path
from .views import find_project


urlpatterns = [
    path('', find_project, name="find_project" )
    ]