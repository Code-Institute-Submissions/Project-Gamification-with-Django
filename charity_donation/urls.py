from django.urls import path
from .views import charity_donation

urlpatterns = [
    path('', charity_donation, name ='charity_donation'),
    ]