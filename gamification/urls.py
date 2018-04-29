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
from accounts.views import index
from accounts import urls as accounts_urls
from projects import urls as projects_urls
from kickstart_project import urls as kickstart_project_urls
from projects.views import all_projects
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_projects, name="index"),
    path('accounts/', include(accounts_urls)),
    path('projects/', include(projects_urls)),
    path('kickstart/', include(kickstart_project_urls)),
    path('media/<path>', static.serve, {'document_root': MEDIA_ROOT}),

]
