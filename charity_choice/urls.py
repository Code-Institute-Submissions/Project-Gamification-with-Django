from django.urls import path
from .views import add_to_donations, adjust_donations, charities, propose_charity, delete_charity, view_donations

urlpatterns = [
    path('charities', charities, name="charities"),                             ## charities
    path('propose_charity/', propose_charity, name='propose_charity'),          ## add new charity
    path('delete_charity/<int:pk>', delete_charity, name='delete_charity'),     ## delete charity
    path('support/<id>', add_to_donations, name="add_to_donations"),            ## donate 
    path('adjust/<id>', adjust_donations, name="adjust_donations"),             ## remove charity from user donation list
    path('view_donations', view_donations, name="view_donations")               ## user's chosen donation
    ]