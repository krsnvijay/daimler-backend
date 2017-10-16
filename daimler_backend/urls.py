"""daimler_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from app import views
from app.views import upload_file

schema_view = get_schema_view(title='Daimler API')
router = routers.DefaultRouter()
router.register(r'parts', views.PartViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title='Daimler API Documentation')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^upload_file/', upload_file, name='upload_file')
]
