"""Defines  a url pattern for users"""
from django.urls import path, include

app_name = 'urls'
urlpatterns = [
    # Include Default auth urls.
    path('', include('django.contrib.auth.urls'))
]
