"""Defines URLs pattern for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Page That shows all the topics
    path('topics/', views.topics, name='topics'),
]
