from django import forms
from .models import Bitacora, Cirugia, Medicamento, Propietario, Mascota, Cita

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


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'descripcion', 'cantidad', 'fecha_venc']
        widgets = {
            'nombre':      forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'cantidad':    forms.NumberInput(attrs={'class':'form-control'}),
            'fecha_venc':  forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }


class CirugiaForm(forms.ModelForm):
    class Meta:
        model = Cirugia
        fields = ['mascota', 'veterinario', 'fecha_plan', 'descripcion']
        widgets = {
            'mascota':     forms.Select(attrs={'class':'form-select'}),
            'veterinario': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_plan':  forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
        }


class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = ['cita', 'observacion', 'tratamiento']
        widgets = {
            'cita':        forms.Select(attrs={'class':'form-select'}),
            'observacion': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'tratamiento': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
        }