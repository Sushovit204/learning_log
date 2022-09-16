"""Defines  a url pattern for users"""
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include Default auth urls.
    path('', include('django.contrib.auth.urls'))
]
