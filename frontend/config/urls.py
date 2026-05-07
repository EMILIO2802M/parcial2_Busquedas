"""
URL configuration for config project.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('menu_app.urls')),
]
