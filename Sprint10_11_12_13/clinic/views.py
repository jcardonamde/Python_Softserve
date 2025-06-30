import csv
import logging
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Propietario, Mascota, Cita, Medicamento, Cirugia, Bitacora
from .forms import PropietarioForm, MascotaForm, CitaForm, MedicamentoForm, CirugiaForm, BitacoraForm
from .utils import export_to_csv

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'clinic/home.html')


def services(request):
    return render(request, 'clinic/services.html')


def placeholder(request):
    context = {
        'items': ['Mascotas', 'Citas', 'Dueños']
    }
    return render(request, 'clinic/placeholder.html', context)


# — Propietarios —
def propietario_list(request):
    try:
        lista = Propietario.objects.all()
        logger.info("Listado de propietarios (%d)", lista.count())
        return render(request, 'clinic/propietario_list.html', {'propietarios': lista})
    except Exception as e:
        logger.error("Error al obtener propietarios: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {
            'message': 'No se pudieron listar los propietarios.'
        }, status=500)


def propietario_create(request):
    try:
        if request.method == 'POST':
            form = PropietarioForm(request.POST)
            if form.is_valid():
                p = form.save()
                logger.info("Propietario creado: %s (ID=%d)", p.nombre, p.pk)
                return redirect('propietario_list')
        else:
            form = PropietarioForm()
            
        return render(request, 'clinic/propietario_form.html', {'form': form})
    except Exception as e:
        logger.error("Error al crear propietario: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {
            'message': 'No se pudo crear el propietario.'
        }, status=500)


# — Mascotas —
def mascota_list(request):
    try:
        lista = Mascota.objects.select_related('propietario').all()
        logger.info("Listado de mascotas (%d)", lista.count())
        return render(request, 'clinic/mascota_list.html', {'mascotas': lista})
    except Exception as e:
        logger.error("Error al obtener mascotas: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {
            'message': 'No se pudieron listar las mascotas.'
        }, status=500)


def mascota_create(request):
    try:
        if request.method == 'POST':
            form = MascotaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mascota_list')
        else:
            form = MascotaForm()
        return render(request, 'clinic/mascota_form.html', {'form': form})
    except Exception as e:
        logger.error("Error en mascota_create: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo crear la mascota.'}, status=500)


# — Citas —
def cita_list(request):
    try:
        lista = Cita.objects.select_related('mascota').all()
        logger.info("Listado de citas (%d)", lista.count())
        return render(request, 'clinic/cita_list.html', {'citas': lista})
    except Exception as e:
        logger.error("Error al obtener citas: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {
            'message': 'No se pudieron listar las citas.'
        }, status=500)


def cita_create(request):
    try:
        if request.method == 'POST':
            form = CitaForm(request.POST)
            if form.is_valid():
                c = form.save()
                logger.info("Cita creada: %s (ID=%d)", c, c.pk)
                return redirect('cita_list')
        else:
            form = CitaForm()
        return render(request, 'clinic/cita_form.html', {'form': form})
    except Exception as e:
        logger.error("Error en cita_create: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo crear la cita.'}, status=500)


# --- CRUD Medicamentos ---
def medicamento_list(request):
    try:
        meds = Medicamento.objects.all()
        logger.info("Listado de medicamentos (%d)", meds.count())
        return render(request, "medications/medicamento_list.html", {"medicamentos": meds})
    except Exception as e:
        logger.error("Error en medicamento_list: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudieron listar los medicamentos.'}, status=500)


def medicamento_create(request):
    try:
        if request.method == 'POST':
            form = MedicamentoForm(request.POST)
            if form.is_valid():
                m = form.save()
                logger.info("Medicamento creado: %s (ID=%d)", m.nombre, m.pk)
                return redirect("medicamento_list")
        else:
            form = MedicamentoForm()
        return render(request, "medications/medicamento_form.html", {"form": form})
    except Exception as e:
        logger.error("Error en medicamento_create: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo crear el medicamento.'}, status=500)


def medicamento_update(request, pk):
    try:
        med = get_object_or_404(Medicamento, pk=pk)
        form = MedicamentoForm(request.POST or None, instance=med)
        if form.is_valid():
            m = form.save()
            logger.info("Medicamento actualizado: %s (ID=%d)", m.nombre, m.pk)
            return redirect("medicamento_list")
        return render(request, "medications/medicamento_form.html", {"form": form})
    except Exception as e:
        logger.error("Error en medicamento_update: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo actualizar el medicamento.'}, status=500)


def medicamento_delete(request, pk):
    try:
        med = get_object_or_404(Medicamento, pk=pk)
        if request.method == "POST":
            med.delete()
            logger.info("Medicamento eliminado: %s (ID=%d)", med.nombre, med.pk)
            return redirect("medicamento_list")
        return render(request, "medications/medicamento_confirm_delete.html", {"medicamento": med})
    except Exception as e:
        logger.error("Error en medicamento_delete: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo eliminar el medicamento.'}, status=500)


# --- CRUD Cirugías ---
def cirugia_list(request):
    try:
        cirs = Cirugia.objects.select_related("mascota").all()
        logger.info("Listado de cirugías (%d)", cirs.count())
        return render(request, "surgeries/cirugia_list.html", {"cirugias": cirs})
    except Exception as e:
        logger.error("Error en cirugia_list: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudieron listar las cirugías.'}, status=500)


def cirugia_create(request):
    try:
        if request.method == 'POST':
            form = CirugiaForm(request.POST or None)
            if form.is_valid():
                c = form.save()
                logger.info("Cirugía programada: %s (ID=%d)", c, c.pk)
                return redirect("cirugia_list")
        else:
            form = CirugiaForm()    
        return render(request, "surgeries/cirugia_form.html", {"form": form})
    except Exception as e:
        logger.error("Error en cirugia_create: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo programar la cirugía.'}, status=500)


def cirugia_update(request, pk):
    try:
        cir = get_object_or_404(Cirugia, pk=pk)
        form = CirugiaForm(request.POST or None, instance=cir)
        if form.is_valid():
            form.save()
            logger.info("Cirugía actualizada: %s (ID=%d)", cir, cir.pk)
            return redirect("cirugia_list")
        return render(request, "surgeries/cirugia_form.html", {"form": form})
    except Exception as e:
        logger.error("Error en cirugia_update: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo actualizar la cirugía.'}, status=500)
    

def cirugia_delete(request, pk):
    try:
        cir = get_object_or_404(Cirugia, pk=pk)
        if request.method == "POST":
            cir.delete()
            logger.info("Cirugía eliminada: %s (ID=%d)", cir, cir.pk)
            return redirect("cirugia_list")
        return render(request, "surgeries/cirugia_confirm_delete.html", {"cirugia": cir})
    except Exception as e:
        logger.error("Error en cirugia_delete: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo eliminar la cirugía.'}, status=500)


# --- CRUD Bitácoras ---
def bitacora_list(request):
    try:
        logs = Bitacora.objects.select_related("cita__mascota").all()
        logger.info("Listado de bitácoras (%d)", logs.count())
        return render(request, "logs/bitacora_list.html", {"bitacoras": logs})
    except Exception as e:
        logger.error("Error en bitacora_list: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudieron listar las bitácoras.'}, status=500)


def bitacora_create(request):
    try:
        if request.method == 'POST':
            form = BitacoraForm(request.POST)
            if form.is_valid():
                b = form.save()
                logger.info("Bitácora creada: ID=%d", b.pk)
                return redirect("bitacora_list")
        else:
            form = BitacoraForm()
        return render(request, "logs/bitacora_form.html", {"form": form})
    except Exception as e:
        logger.error("Error en bitacora_create: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo crear la bitácora.'}, status=500)


def bitacora_update(request, pk):
    try:
        log = get_object_or_404(Bitacora, pk=pk)
        form = BitacoraForm(request.POST or None, instance=log)
        if form.is_valid():
            form.save()
            logger.info("Bitácora actualizada: ID=%d", log.pk)
            return redirect("bitacora_list")
        return render(request, "logs/bitacora_form.html", {"form": form})
    except Exception as e:
        logger.error("Error en bitacora_update: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo actualizar la bitácora.'}, status=500)


def bitacora_delete(request, pk):
    try:
        b = get_object_or_404(Bitacora, pk=pk)
        if request.method == "POST":
            b.delete()
            logger.info("Bitácora eliminada: ID=%d", b, b.pk)
            return redirect("bitacora_list")
        return render(request, "logs/bitacora_confirm_delete.html", {"bitacora": b})
    except Exception as e:
        logger.error("Error en bitacora_delete: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo eliminar la bitácora.'}, status=500)


# --- Historia Clínica ---
def historia_index(request):
    """
    Muestra una lista de mascotas para seleccionar
    y ver su historia clínica.
    """
    try:
        mascotas = Mascota.objects.select_related('propietario').all()
        logger.info("Mostrando selector de historia clínica (%d mascotas)", mascotas.count())
        return render(request, 'clinic/historia_index.html', {
            'mascotas': mascotas
        })
    except Exception as e:
        logger.error("Error al obtener mascotas: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {
            'message': 'No se pudieron listar las mascotas.'
        }, status=500)


def historia_clinica(request, mascota_id):
    try:
        mascota  = get_object_or_404(Mascota, pk=mascota_id)
        bitacoras = Bitacora.objects.filter(cita__mascota=mascota).order_by('creada_en')
        context = {
            'mascota': mascota,
            'bitacoras': bitacoras,
        }
        logger.info("Mostrando historia clínica para mascota ID %d", mascota_id)
        return render(request, 'clinic/historia_clinica.html', context)
    except Exception as e:
        logger.error("Error en historia_clinica: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {
            'message': 'No se pudo generar la historia clínica.'
        }, status=500)


# --- Exportar CSV ---
def export_propietarios_csv(request):
    try:
        qs = Propietario.objects.all()
        return export_to_csv(
            qs,
            ['ID','Nombre','Teléfono','Email'],
            'propietarios.csv',
            lambda p: [p.id, p.nombre, p.telefono, p.email]
        )
    except Exception as e:
        logger.error("Error en export_propietarios_csv: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo exportar propietarios.'}, status=500)
    

def export_mascotas_csv(request):
    try:
        qs = Mascota.objects.select_related('propietario').all()
        return export_to_csv(
            qs,
            ['ID','Nombre','Especie','Edad','Propietario'],
            'mascotas.csv',
            lambda m: [m.id, m.nombre, m.especie, m.edad, m.propietario.nombre]
        )
    except Exception as e:
        logger.error("Error en export_mascotas_csv: %s", e, exc_info=True)
        return render(request, 'clinic/error.html', {'message': 'No se pudo exportar mascotas.'}, status=500)
