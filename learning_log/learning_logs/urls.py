from django.urls import path
from . import views
"""Defines url patterns for learning_log."""
urlpatterns = [
#Homepage
url(r'^$',views.ndex,name='index')
    
]