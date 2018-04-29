from django.conf.urls import url, include
from django.urls import path
from accounts.views import index, logout, login, register, user_dashboard
from accounts import url_reset


urlpatterns = [
    path('logout/', logout, name = "logout"),
    path('login/', login, name = "login"),
    path('register/', register, name="registration"),
    path('user_dashboard/', user_dashboard, name = "user_dashboard"),
    path('password-reset/', include(url_reset))

]
