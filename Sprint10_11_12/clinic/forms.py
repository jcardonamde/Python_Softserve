from django import forms
from .models import Propietario, Mascota, Cita

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


# Formulario para el modelo Cita
# Este formulario permite crear y editar citas para mascotas
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['mascota','fecha','motivo','diagnostico']
        widgets = {
            'mascota':    forms.Select(attrs={'class': 'form-select'}),
            'fecha':      forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control'}),
            'motivo':     forms.TextInput(attrs={'class':'form-control'}),
            'diagnostico':forms.TextInput(attrs={'class':'form-control'}),
        }
