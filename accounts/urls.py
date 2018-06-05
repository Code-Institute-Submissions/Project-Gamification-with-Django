from django.urls import path, include
from . import urls_reset
from .views import *

urlpatterns = [
    path('profile/<int:pk>', profile, name='profile'),
    path('issue_fixed/<int:pk>', issue_fixed, name='issue_fixed'),
    path('logout/', logout, name='logout'),
    path('password-reset/', include(urls_reset)),
    path('profile/gamification_test/<int:pk>', gamification_test, name='gamification_test')
    
]
