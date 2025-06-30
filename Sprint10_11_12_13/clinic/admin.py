from django.contrib import admin
from .models import Bitacora, Cirugia, Medicamento, Propietario, Mascota, Cita

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

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'descripcion', 'cantidad', 'fecha_venc')
    list_filter   = ('fecha_venc',)
    search_fields = ('nombre',)

@admin.register(Cirugia)
class CirugiaAdmin(admin.ModelAdmin):
    list_display  = ('mascota', 'veterinario', 'fecha_plan', 'descripcion')
    list_filter   = ('fecha_plan', 'veterinario')
    search_fields = ('mascota__nombre', 'veterinario')

@admin.register(Bitacora)
class BitacoraAdmin(admin.ModelAdmin):
    list_display  = ('id', 'cita', 'observacion', 'tratamiento', 'creada_en')
    list_filter   = ('creada_en',)
    search_fields = ('cita__mascota__nombre',)