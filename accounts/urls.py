from django.urls import path, include
from . import urls_reset
from .views import login_page, profile, logout, my_details, issue_fixed

urlpatterns = [

    path('profile/<int:pk>', profile, name='profile'),
    path('issue_fixed/<int:pk>', issue_fixed, name='issue_fixed'),
    path('my_details/<int:pk>', my_details, name='my_details'),
    path('logout/', logout, name='logout'),
    path('password-reset/', include(urls_reset)),
    
]
