import csv
import logging
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Propietario, Mascota, Cita, Medicamento, Cirugia, Bitacora
from .forms import PropietarioForm, MascotaForm, CitaForm, MedicamentoForm, CirugiaForm, BitacoraForm

logger = logging.getLogger(__name__)

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


# --- CRUD Medicamentos ---
def medicamento_list(request):
    meds = Medicamento.objects.all()
    return render(request, "clinic/medicamento_list.html", {"medicamentos": meds})


def medicamento_create(request):
    form = MedicamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        logger.info("Medicamento creado: %s", form.instance)
        return redirect("medicamento_list")
    return render(request, "clinic/medicamento_form.html", {"form": form})


def medicamento_update(request, pk):
    med = get_object_or_404(Medicamento, pk=pk)
    form = MedicamentoForm(request.POST or None, instance=med)
    if form.is_valid():
        form.save()
        logger.info("Medicamento actualizado: %s", med)
        return redirect("medicamento_list")
    return render(request, "clinic/medicamento_form.html", {"form": form})


def medicamento_delete(request, pk):
    med = get_object_or_404(Medicamento, pk=pk)
    if request.method == "POST":
        med.delete()
        logger.info("Medicamento eliminado: %s", med)
        return redirect("medicamento_list")
    return render(request, "clinic/medicamento_confirm_delete.html", {"medicamento": med})


# --- CRUD Cirugías ---
def cirugia_list(request):
    cirs = Cirugia.objects.select_related("mascota").all()
    return render(request, "clinic/cirugia_list.html", {"cirugias": cirs})


def cirugia_create(request):
    form = CirugiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        logger.info("Cirugía programada: %s", form.instance)
        return redirect("cirugia_list")
    return render(request, "clinic/cirugia_form.html", {"form": form})


def cirugia_update(request, pk):
    cir = get_object_or_404(Cirugia, pk=pk)
    form = CirugiaForm(request.POST or None, instance=cir)
    if form.is_valid():
        form.save()
        logger.info("Cirugía actualizada: %s", cir)
        return redirect("cirugia_list")
    return render(request, "clinic/cirugia_form.html", {"form": form})


def cirugia_delete(request, pk):
    cir = get_object_or_404(Cirugia, pk=pk)
    if request.method == "POST":
        cir.delete()
        logger.info("Cirugía eliminada: %s", cir)
        return redirect("cirugia_list")
    return render(request, "clinic/cirugia_confirm_delete.html", {"cirugia": cir})


# --- CRUD Bitácoras ---
def bitacora_list(request):
    logs = Bitacora.objects.select_related("cita__mascota").all()
    return render(request, "clinic/bitacora_list.html", {"bitacoras": logs})


def bitacora_create(request):
    form = BitacoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        logger.info("Bitácora registrada: %s", form.instance)
        return redirect("bitacora_list")
    return render(request, "clinic/bitacora_form.html", {"form": form})


def bitacora_update(request, pk):
    log = get_object_or_404(Bitacora, pk=pk)
    form = BitacoraForm(request.POST or None, instance=log)
    if form.is_valid():
        form.save()
        logger.info("Bitácora actualizada: %s", log)
        return redirect("bitacora_list")
    return render(request, "clinic/bitacora_form.html", {"form": form})


def bitacora_delete(request, pk):
    log = get_object_or_404(Bitacora, pk=pk)
    if request.method == "POST":
        log.delete()
        logger.info("Bitácora eliminada: %s", log)
        return redirect("bitacora_list")
    return render(request, "clinic/bitacora_confirm_delete.html", {"bitacora": log})


# --- Historia Clínica ---
def historia_clinica(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    bitacoras = Bitacora.objects.filter(cita__mascota=mascota).order_by("creada_en")
    return render(request, "clinic/historia_clinica.html", {
        "mascota": mascota,
        "bitacoras": bitacoras,
    })


# --- Exportar CSV ---
def export_propietarios_csv(request):
    qs = Propietario.objects.all()
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="propietarios.csv"'
    writer = csv.writer(response)
    writer.writerow(["ID", "Nombre", "Teléfono", "Email"])
    for p in qs:
        writer.writerow([p.id, p.nombre, p.telefono, p.email])
    logger.info("Exportados %d propietarios a CSV", qs.count())
    return response


def export_mascotas_csv(request):
    qs = Mascota.objects.select_related("propietario").all()
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="mascotas.csv"'
    writer = csv.writer(response)
    writer.writerow(["ID", "Nombre", "Especie", "Edad", "Propietario"])
    for m in qs:
        writer.writerow([m.id, m.nombre, m.especie, m.edad, m.propietario.nombre])
    logger.info("Exportadas %d mascotas a CSV", qs.count())
    return response
