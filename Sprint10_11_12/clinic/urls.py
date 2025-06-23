from django.urls import path
from . import views

urlpatterns = [
    # Páginas estáticas
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('placeholder/', views.placeholder, name='placeholder'),
    # CRUD Propietarios
    path('owners/', views.propietario_list,  name='propietario_list'),
    path('owners/new/', views.propietario_create, name='propietario_create'),
    # CRUD Mascotas
    path('pets/', views.mascota_list,   name='mascota_list'),
    path('pets/new/', views.mascota_create, name='mascota_create'),
    # CRUD Citas
    path('appointments/',     views.cita_list,    name='cita_list'),
    path('appointments/new/', views.cita_create,  name='cita_create'),
    # Medicamentos CRUD
    path('medicines/', views.medicamento_list, name='medicamento_list'),
    path('medicines/new/', views.medicamento_create, name='medicamento_create'),
    path('medicines/<int:pk>/edit/', views.medicamento_update, name='medicamento_update'),
    path('medicines/<int:pk>/delete/', views.medicamento_delete, name='medicamento_delete'),
    # Cirugías CRUD
    path('surgeries/', views.cirugia_list, name='cirugia_list'),
    path('surgeries/new/', views.cirugia_create, name='cirugia_create'),
    path('surgeries/<int:pk>/edit/', views.cirugia_update, name='cirugia_update'),
    path('surgeries/<int:pk>/delete/', views.cirugia_delete, name='cirugia_delete'),
    # Bitácora CRUD
    path('logs/', views.bitacora_list, name='bitacora_list'),
    path('logs/new/', views.bitacora_create, name='bitacora_create'),
    path('logs/<int:pk>/edit/', views.bitacora_update, name='bitacora_update'),
    path('logs/<int:pk>/delete/', views.bitacora_delete, name='bitacora_delete'),
    # Historia clínica
    path('history/<int:mascota_id>/', views.historia_clinica, name='historia_clinica'),
    # Exportaciones CSV
    path('export/owners/',   views.export_propietarios_csv, name='export_propietarios_csv'),
    path('export/pets/',     views.export_mascotas_csv,     name='export_mascotas_csv'),
]
