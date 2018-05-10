from django.urls import path, include
from . import urls_reset
from .views import index, user_login, profile, logout, my_details

urlpatterns = [
    path('user_login/', user_login, name='user_login'),
    path('profile/', profile, name='profile'),
    path('my_details/<str:owner>', my_details, name='my_details'),
    path('logout/', logout, name='logout'),
    path('password-reset/', include(urls_reset)),
]
