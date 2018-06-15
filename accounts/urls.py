from django.urls import path, include
from . import urls_reset
from .views import *

urlpatterns = [
    path('profile/<int:pk>', profile, name='profile'),                                      ## user porfile
    path('issue_fixed/<int:pk>', issue_fixed, name='issue_fixed'),                          ## fixed issue  
    path('logout/', logout, name='logout'),                                                 ## logout
    path('password-reset/', include(urls_reset)),                                           ## reset password
    path('profile/gamification_test/<int:pk>', gamification_test, name='gamification_test') ## gamification personality test
    
]
