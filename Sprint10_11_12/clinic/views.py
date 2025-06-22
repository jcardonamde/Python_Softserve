from django.shortcuts import render, redirect
from .models import Propietario, Mascota, Cita
from .forms import PropietarioForm, MascotaForm, CitaForm

# Create your views here.
def home(request):
    return render(request, 'clinic/home.html')


def services(request):
    return render(request, 'clinic/services.html')


def placeholder(request):
    # Ejemplo de contexto dinámico mínimo
    context = {
        'items': ['Mascotas', 'Citas', 'Dueños']
    }
    return render(request, 'clinic/placeholder.html', context)


# — Propietarios —
def propietario_list(request):
    lista = Propietario.objects.all()
    return render(request, 'clinic/propietario_list.html', {'propietarios': lista})


def propietario_create(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propietario_list')
    else:
        form = PropietarioForm()
    return render(request, 'clinic/propietario_form.html', {'form': form})


# — Mascotas —
def mascota_list(request):
    lista = Mascota.objects.select_related('propietario').all()
    return render(request, 'clinic/mascota_list.html', {'mascotas': lista})


def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota_list')
    else:
        form = MascotaForm()
    return render(request, 'clinic/mascota_form.html', {'form': form})


# — Citas —
def cita_list(request):
    lista = Cita.objects.select_related('mascota').all()
    return render(request, 'clinic/cita_list.html', {'citas': lista})


def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cita_list')
    else:
        form = CitaForm()
    return render(request, 'clinic/cita_form.html', {'form': form})
