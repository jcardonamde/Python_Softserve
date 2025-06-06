import os
import sys
import csv
import json
import logging
from datetime import datetime
from typing import List, Tuple

from models import Dueno, Mascota, Consulta


# --- Determinar directorio base (ubicación del script) y rutas de archivos ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'clinica_veterinaria.log')
CSV_MASCOTAS = os.path.join(BASE_DIR, 'mascotas_dueños.csv')
JSON_CONSULTAS = os.path.join(BASE_DIR, 'consultas.json')


# Configurar logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info('Inicio de la aplicación (storage)')


# --- Funciones de Serialización / Deserialización ---
# Guardar y cargar mascotas y dueños en CSV
def guardar_mascotas_csv(mascotas: List[Mascota]) -> None:
    """
    Guarda las mascotas y dueños en un archivo CSV.
    Columnas: nombre_mascota, especie, raza, edad, nombre_dueno, telefono, direccion
    """
    try:
        with open(CSV_MASCOTAS, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['nombre_mascota','especie','raza','edad','nombre_dueno','telefono','direccion'])
            for m in mascotas:
                writer.writerow([
                    m.nombre, m.especie, m.raza, m.edad,
                    m.dueno.nombre, m.dueno.telefono, m.dueno.direccion
                ])
        logging.info(f"Se exportaron {len(mascotas)} mascotas a {CSV_MASCOTAS}")
    except Exception as e:
        logging.error(f"Error al guardar mascotas CSV: {e}")


# Cargar mascotas y dueños desde el CSV
def cargar_mascotas_csv() -> List[Mascota]:
    """
    Carga mascotas y dueños desde el CSV.
    Si no existe el archivo, devuelve lista vacía.
    """
    mascotas: List[Mascota] = []
    if not os.path.exists(CSV_MASCOTAS):
        logging.warning(f"Archivo {CSV_MASCOTAS} no encontrado, cargando lista vacía.")
        return mascotas

    try:
        with open(CSV_MASCOTAS, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dueno = Dueno(row['nombre_dueno'], row['telefono'], row['direccion'])
                mascota = Mascota(
                    row['nombre_mascota'], row['especie'], row['raza'],
                    int(row['edad']), dueno
                )
                mascotas.append(mascota)
        logging.info(f"Se cargaron {len(mascotas)} mascotas desde {CSV_MASCOTAS}")
    except Exception as e:
        logging.error(f"Error al cargar mascotas CSV: {e}")
    return mascotas


# Guardar y cargar consultas en JSON
def guardar_consultas_json(consultas: List[Consulta]) -> None:
    """
    Guarda las consultas en un archivo JSON.
    Cada consulta se serializa con los campos: fecha, motivo, diagnostico, nombre_mascota
    """
    try:
        datos = []
        for c in consultas:
            datos.append({
                'fecha': c.fecha.isoformat(),
                'motivo': c.motivo,
                'diagnostico': c.diagnostico,
                'nombre_mascota': c.mascota.nombre
            })
        with open(JSON_CONSULTAS, mode='w', encoding='utf-8') as file:
            json.dump(datos, file, indent=2, ensure_ascii=False)
        logging.info(f"Se exportaron {len(consultas)} consultas a {JSON_CONSULTAS}")
    except Exception as e:
        logging.error(f"Error al guardar consultas JSON: {e}")


# Cargar consultas desde el JSON
def cargar_consultas_json(mascotas: List[Mascota]) -> List[Consulta]:
    """
    Carga las consultas desde el JSON.
    Relaciona cada consulta con la instancia de Mascota por nombre.
    Si no existe archivo, devuelve lista vacía.
    """
    consultas: List[Consulta] = []
    if not os.path.exists(JSON_CONSULTAS):
        logging.warning(f"Archivo {JSON_CONSULTAS} no encontrado, cargando lista vacía.")
        return consultas

    try:
        with open(JSON_CONSULTAS, mode='r', encoding='utf-8') as file:
            datos = json.load(file)
            for item in datos:
                # Buscar mascota por nombre
                nombre = item.get('nombre_mascota')
                pet = next((m for m in mascotas if m.nombre == nombre), None)
                if pet:
                    fecha = datetime.fromisoformat(item.get('fecha'))
                    consulta = Consulta(fecha, item.get('motivo',''), item.get('diagnostico',''), pet)
                    consultas.append(consulta)
                else:
                    logging.warning(f"Consulta para mascota no registrada: {nombre}")
        logging.info(f"Se cargaron {len(consultas)} consultas desde {JSON_CONSULTAS}")
    except Exception as e:
        logging.error(f"Error al cargar consultas JSON: {e}")
    return consultas
