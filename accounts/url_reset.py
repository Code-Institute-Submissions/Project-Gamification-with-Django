from django.conf.urls import url
from django.urls import path, reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('done/', password_reset_done, name='password_reset_done'),
    path('<slug:uidb64>/<slug:token>)/', password_reset_confirm, {'post_reset_confirm': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('complete/', password_reset_complete, name='password_reset_complete')
    ]