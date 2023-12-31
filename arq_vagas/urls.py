"""
URL configuration for arq_vagas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from apps.core.views import *
from apps.blog.views import *
from apps.jobs.views import *
from django.conf import settings
from django.conf.urls.static import static

# http://127.0.0.1:8000/

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    path('core/', include('apps.core.urls')),
    path('jobs/', include('apps.jobs.urls')),
    path('blog/', include('apps.blog.urls')),
    # http://127.0.0.1:8000/
    path('', home, name="pagina_home"),
    path('grappelli/', include('grappelli.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

















    