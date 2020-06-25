# -*- coding: utf-8 -*-
from django.urls import path, include
from basic_app import views

# Template tagging- Django will automatically search for app_name
app_name = 'basic_app' #tell django to find url that matches from basic_app

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    
    ]


