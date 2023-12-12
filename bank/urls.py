"""
URL configuration for bank project.

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
from django.urls import path,include
from rest_framework import routers
from services import views
from django.urls import re_path as url

router = routers.DefaultRouter()
router.register(r'upload', views.DatabaseViewSet, basename="upload")
router.register(r'client', views.ClientViewSet, basename="client")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url('^csv-uploader/$', views.CsvUploader.as_view(), name='csv-uploader'),
    url('^csv-uploader2/$', views.CsvUploader2.as_view(), name='csv-uploader2'),
    url('^csv-uploader3/$', views.CsvUploader3.as_view(), name='csv-uploader3'),
]
