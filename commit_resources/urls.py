from django.urls import path
from .views import finalize_donation

urlpatterns = [
    path('', finalize_donation, name ='finalize_donation'),
    ]