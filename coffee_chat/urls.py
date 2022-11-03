from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.application_list),
    path('/<int:pk>', views.application_write),
]
