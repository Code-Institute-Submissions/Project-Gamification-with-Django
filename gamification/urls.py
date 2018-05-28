"""gamification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from accounts.views import login_page
from accounts import urls as accounts_urls
from projects import urls as projects_urls
from charity_choice import urls as charity_choice_urls
from project_search import urls as project_search_urls
from donate import urls as donate_urls
from projects.views import all_projects
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name="login_page"),
    path('accounts/', include(accounts_urls)),
    path('projects/', include(projects_urls)),
    path('charity_choice/', include(charity_choice_urls)),
    path('find_project/', include(project_search_urls)),
    path('finalize_donation/', include(donate_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),

]
