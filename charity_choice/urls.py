from django.urls import path
from .views import add_to_donations, adjust_donations, charities, propose_charity, delete_charity, view_donations

urlpatterns = [
    path('charities', charities, name="charities"),
    path('propose_charity/', propose_charity, name='propose_charity'),
    path('delete_charity/<int:pk>', delete_charity, name='delete_charity'),
    path('support/<id>', add_to_donations, name="add_to_donations"),
    path('adjust/<id>', adjust_donations, name="adjust_donations"),
    path('view_donations', view_donations, name="view_donations")
    ]