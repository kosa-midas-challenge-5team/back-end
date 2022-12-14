"""kosa_midas_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import *
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('accounts', views.account_list),
    path('accounts/<int:pk>', views.account),
    path('login', views.login),
    path('', views.index),
    path('admin/', views.admin),
    path('admin/modify', views.modify),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]