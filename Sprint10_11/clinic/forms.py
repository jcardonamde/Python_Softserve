from django import forms
from .models import Propietario
from .models import Mascota

# Formulario para el modelo Propietario
# Este formulario permite crear y editar propietarios de mascotas
class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'telefono', 'email']


# Formulario para el modelo Mascota
# Este formulario permite crear y editar mascotas asociadas a un propietario
class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'propietario']