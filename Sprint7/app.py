"""
Ejercicio Sprint7: Sistema Completo de Gestión para Veterinaria con Pruebas Unitarias

Extiende el sistema de gestión con sus funcionalidades actuales para incorporar 
pruebas unitarias utilizando el módulo unittest de Python - Clínica Veterinaria "Amigos Peludos"

Autores: Jonathan Cardona Calderon - Sandra Liliana Zapata Gallón
"""

import sys
import logging
from datetime import datetime
from typing import List, Tuple

from models import Dueno, Mascota, Consulta
from storage import (
    guardar_mascotas_csv,
    cargar_mascotas_csv,
    guardar_consultas_json,
    cargar_consultas_json
)
from utils import input_int


# Configuramos logging en caso de que se importe directamente app.py
# (Nota: storage.py ya configura el logger, pero para un logger adicional para 'app',lo hacemos aquí).
logger = logging.getLogger(__name__)
logger.info("Arrancando la aplicación (app.py)")


# --- Funciones del menú con manejo de excepciones --
def mostrar_menu() -> str:
    print("\n=== Clínica Veterinaria Amigos Peludos ===")
    print("1. Registrar mascota")
    print("2. Registrar consulta")
    print("3. Listar mascotas")
    print("4. Ver historial de consultas")
    print("5. Exportar datos (CSV/JSON)")
    print("6. Importar datos (CSV/JSON)")
    print("7. Salir")
    return input("Seleccione una opción: ").strip()


def registrar_mascota(mascotas: List[Mascota]) -> None:
    """
    Solicita datos para crear una nueva mascota y su dueño.
    Maneja excepciones y registra eventos.
    """
    try:
        print("\n-- Registrar nueva mascota --")
        nombre = input("Nombre de la mascota: ").strip()
        especie = input("Especie: ").strip()
        raza = input("Raza: ").strip()
        edad = input_int("Edad (años): ", min_val=0)

        print("\nDatos del dueño:")
        nombre_d = input("  Nombre: ").strip()
        telefono = input("  Teléfono: ").strip()
        direccion = input("  Dirección: ").strip()

        dueno = Dueno(nombre_d, telefono, direccion)
        mascota = Mascota(nombre, especie, raza, edad, dueno)
        mascotas.append(mascota)
        msg = f"\n Mascota '{nombre}' registrada correctamente."
        print(f"\n {msg}")
        logging.info(msg)
    except Exception as e:
        print(f"Error al registrar la mascota: {e}")
        logging.error(f"Excepción en función registrar_mascota: {e}")


def listar_mascotas(mascotas: List[Mascota]) -> None:
    """
    Muestra todas las mascotas registradas.
    """
    print("\n-- Mascotas registradas --")
    if not mascotas:
        msg = "No hay mascotas registradas."
        print(msg)
        logging.info(msg)
        return
    for i, m in enumerate(mascotas, start=1):
        print(f"{i}. {m}")


def registrar_consulta(mascotas: List[Mascota], consultas: List[Consulta]) -> None:
    """
    Registra una consulta para una mascota existente.
    Maneja selección inválida y registra eventos.
    """

    try:
        print("\n-- Registrar consulta veterinaria --")
        if not mascotas:
            raise IndexError("No hay mascotas registradas.")

        listar_mascotas(mascotas)
        idx = input_int("Seleccione el número de la mascota: ", min_val=1, max_val=len(mascotas)) - 1
        motivo = input("Motivo de la consulta: ").strip()
        diagnostico = input("Diagnóstico: ").strip()
        fecha = datetime.now()

        consulta = Consulta(fecha, motivo, diagnostico, mascotas[idx])
        consultas.append(consulta)
        msg = f"\n Consulta registrada para '{mascotas[idx].nombre}'."
        print(f"\n {msg}")
        logging.info(msg)
    except IndexError as ie:
        print("\n-- Registrar consulta veterinaria --")
        logging.warning(f"Intento de consulta inválido: {ie}")
    except Exception as e:
        print(f"Error al registrar la consulta: {e}")
        logging.error(f"Excepción en función registrar_consulta: {e}")


def ver_historial(mascotas: List[Mascota], consultas: List[Consulta]) -> None:
    """
    Muestra el historial de consultas de una mascota específica.
    Maneja selección inválida.
    """
    try:
        print("\n-- Historial de consultas --")
        if not mascotas:
            raise IndexError("No hay mascotas registradas.")

        listar_mascotas(mascotas)
        idx = input_int("Seleccione el número de la mascota: ", min_val=1, max_val=len(mascotas)) - 1
        pet = mascotas[idx]
        historial = [c for c in consultas if c.mascota is pet]
        if not historial:
            msg = f"No hay consultas registradas para '{pet.nombre}'."
            print(msg)
            logging.info(msg)
        else:
            print(f"\nConsultas de '{pet.nombre}':")
            for c in historial:
                print(c)
            logging.info(f"Historial de consultas mostrado para '{pet.nombre}'.")
    except IndexError as ie:
        print(f"Error: {ie}")
        logging.warning(f"Intento de historial inválido: {ie}")
    except Exception as e:
        print(f"Error al mostrar el historial: {e}")
        logging.error(f"Excepción en función ver_historial: {e}")


# --- Funciones de import/export ---
def exportar_datos(mascotas: List[Mascota], consultas: List[Consulta]) -> None:
    guardar_mascotas_csv(mascotas)
    guardar_consultas_json(consultas)
    print("Datos exportados correctamente.")


def importar_datos() -> Tuple[List[Mascota], List[Consulta]]:
    mascotas = cargar_mascotas_csv()
    consultas = cargar_consultas_json(mascotas)
    print("Datos importados correctamente.")
    return mascotas, consultas


# --- Bucle principal con manejo manejo global de excepciones ---
def main() -> None:
    # Inicializa listas e intenta carga automática
    try:
        mascotas, consultas = importar_datos()
    except Exception:
        mascotas, consultas = [], []

    try:
        while True:
            opcion = mostrar_menu()
            if opcion == "1":
                registrar_mascota(mascotas)
            elif opcion == "2":
                registrar_consulta(mascotas, consultas)
            elif opcion == "3":
                listar_mascotas(mascotas)
            elif opcion == "4":
                ver_historial(mascotas, consultas)
            elif opcion == "5":
                exportar_datos(mascotas, consultas)
            elif opcion == "6":
                mascotas, consultas = importar_datos()
            elif opcion == "7":
                 # Guardar antes de salir
                exportar_datos(mascotas, consultas)
                print("¡Hasta luego!")
                msg = "Saliendo del programa y guardando datos..."
                logging.info(msg)
                break
            else:
                print("Opción no válida, intente de nuevo.")
                logging.warning(f"Opción inválida en menú: {opcion}")
    except KeyboardInterrupt:
        print("\nInterrupción recibida. Guardando datos y saliendo...")
        logging.info("Interrupción del programa por el usuario.")
        exportar_datos(mascotas, consultas)
        sys.exit(0)
    except Exception as e:
        print(f"Error inesperado: {e}")
        logging.error(f"Excepción no controlada en el bucle principal: {e}")
        exportar_datos(mascotas, consultas)
        sys.exit(1)


# --- Ejecución del programa ---
if __name__ == "__main__":
    main()
