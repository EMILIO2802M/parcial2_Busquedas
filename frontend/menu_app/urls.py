from django.urls import path
from . import views

app_name = 'menu_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('ejecutar/', views.ejecutar_algoritmo, name='ejecutar_algoritmo'),
]
