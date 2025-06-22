from django.contrib import admin
from .models import Propietario, Mascota, Cita

# Register your models here.
@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email')

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'edad', 'propietario')
    list_filter  = ('especie',)

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('mascota','fecha','motivo','diagnostico')
    list_filter  = ('fecha',)
