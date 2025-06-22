from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('placeholder/', views.placeholder, name='placeholder'),
    path('owners/', views.propietario_list,  name='propietario_list'),
    path('owners/new/', views.propietario_create, name='propietario_create'),
    path('pets/', views.mascota_list,   name='mascota_list'),
    path('pets/new/', views.mascota_create, name='mascota_create'),
]
