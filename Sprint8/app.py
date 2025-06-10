"""
Ejercicio Sprint8: Sistema Integral de Gestión para Veterinaria con Persistencia en SQLite

Extiende el sistema de gestión con sus funcionalidades actuales para implementar un sistema
más robusto y eficiente con la finalidad de gestionar y almacenar datos de manera persistente. 
Se ha solicitado implementar almacenamiento utilizando una base de datos SQLite. - Clínica Veterinaria "Amigos Peludos"

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
from database import (
    agregar_dueno,
    listar_duenos,
    actualizar_dueno,
    eliminar_dueno,
    agregar_mascota as db_agregar_mascota,
    listar_mascotas as db_listar_mascotas,
    actualizar_mascota,
    eliminar_mascota,
    agregar_consulta as db_agregar_consulta,
    listar_consultas as db_listar_consultas,
    actualizar_consulta,
    eliminar_consulta
)
from utils import input_int


# Configuramos logging en caso de que se importe directamente app.py
# (Nota: storage.py ya configura el logger, pero para un logger adicional para 'app',lo hacemos aquí).
logger = logging.getLogger(__name__)
logger.info("Arrancando la aplicación (app.py)")


# --- Funciones del menú con manejo de excepciones --
def mostrar_menu() -> str:
    print("\n=== Clínica Veterinaria Amigos Peludos ===")
    print("1. Registrar mascota (memoria)")
    print("2. Registrar consulta (memoria)")
    print("3. Listar mascotas (memoria)")
    print("4. Ver historial (memoria)")
    print("5. Exportar datos (CSV/JSON)")
    print("6. Importar datos (CSV/JSON)")
    print("7. Registrar dueño (SQLite)")
    print("8. Listar dueños (SQLite)")
    print("9. Actualizar dueño (SQLite)")
    print("10. Eliminar dueño (SQLite)")
    print("11. Registrar mascota (SQLite)")
    print("12. Listar mascotas (SQLite)")
    print("13. Actualizar mascota (SQLite)")
    print("14. Eliminar mascota (SQLite)")
    print("15. Registrar consulta (SQLite)")
    print("16. Listar consultas (SQLite)")
    print("17. Actualizar consulta (SQLite)")
    print("18. Eliminar consulta (SQLite)")
    print("19. Salir")
    return input("Seleccione una opción: ").strip()


# --------------------------------------------------
# Funciones para operaciones con Dueños
# --------------------------------------------------
def registrar_dueno_db() -> None:
    print("\n-- Registrar dueño (SQLite) --")
    try:
        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        direccion = input("Dirección: ").strip()
        dueno = Dueno(nombre, telefono, direccion)
        new_id = agregar_dueno(dueno)
        print(f"Dueño insertado con id {new_id}")
        logging.info(f"Dueño registrado en DB con id {new_id}")
    except Exception as e:
        print(f"Error al insertar dueño en DB: {e}")
        logging.error(f"Error registrar_dueno_db: {e}")


def listar_duenos_db() -> None:
    print("\n-- Dueños registrados (SQLite) --")
    duenos = listar_duenos()
    if not duenos:
        print("No hay dueños registrados.")
        return
    for i, (owner_id, dueno) in enumerate(duenos, start=1):
        print(f"{i}. ID {owner_id} | {dueno}")


def actualizar_dueno_db() -> None:
    print("\n-- Actualizar dueño (SQLite) --")
    duenos = listar_duenos()  # List[Tuple[id, Dueno]]
    if not duenos:
        print("No hay dueños para actualizar.")
        return
    for i, (owner_id, dueno) in enumerate(duenos, start=1):
        print(f"{i}. ID {owner_id} | {dueno}")
    idx = input_int("Seleccione dueño (número): ", 1, len(duenos)) - 1
    owner_id, _ = duenos[idx]

    # Pedir nuevos datos
    nombre = input("Nuevo nombre: ").strip()
    telefono = input("Nuevo teléfono: ").strip()
    direccion = input("Nueva dirección: ").strip()
    nuevo = Dueno(nombre, telefono, direccion)

    try:
        actualizar_dueno(owner_id, nuevo)
        print(f"Dueño {owner_id} actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar dueño: {e}")


def eliminar_dueno_db() -> None:
    print("\n-- Eliminar dueño (SQLite) --")
    duenos = listar_duenos()
    if not duenos:
        print("No hay dueños para eliminar.")
        return
    for i, (owner_id, dueno) in enumerate(duenos, start=1):
        print(f"{i}. ID {owner_id} | {dueno}")
    idx = input_int("Seleccione dueño (número): ", 1, len(duenos)) - 1
    owner_id, _ = duenos[idx]

    confirm = input(f"¿Seguro que deseas eliminar el dueño {owner_id}? (s/n): ").lower()
    if confirm == 's':
        try:
            eliminar_dueno(owner_id)
            print(f"Dueño {owner_id} eliminado.")
        except Exception as e:
            print(f"Error al eliminar dueño: {e}")


# --------------------------------------------------
# Funciones para operaciones con Mascotas
# --------------------------------------------------
def registrar_mascota_db() -> None:
    print("\n-- Registrar mascota (SQLite) --")
    duenos = listar_duenos()  
    try:
        if not duenos:
            print("Primero debe registrar un dueño.")
            return
        # Mostrar lista con ids
        for i, (owner_id, d) in enumerate(duenos, start=1):
            print(f"{i}. ({owner_id}) {d}")

        idx = input_int("Seleccione dueño (número): ", 1, len(duenos)) - 1
        owner_id, selected = duenos[idx] # reusamos el id existente

        nombre = input("Nombre de la mascota: ").strip()
        especie = input("Especie: ").strip()
        raza = input("Raza: ").strip()
        edad = input_int("Edad (años): ", 0)

        mascota = Mascota(nombre, especie, raza, edad, selected)
        pet_id = db_agregar_mascota(mascota, owner_id)

        print(f"Mascota insertada en DB con id {pet_id}")
        logging.info(f"Mascota registrada en DB con id {pet_id}")
    except Exception as e:
        print(f"Error al insertar mascota en DB: {e}")
        logging.error(f"Error registrar_mascota_db: {e}")


def listar_mascotas_db() -> None:
    print("\n-- Mascotas registradas (SQLite) --")
    mascotas = db_listar_mascotas()
    if not mascotas:
        print("No hay mascotas registradas.")
        return
    for i, m in enumerate(mascotas, start=1): print(f"{i}. {m}")


def actualizar_mascota_db() -> None:
    print("\n-- Actualizar mascota (SQLite) --")
    mascotas = db_listar_mascotas()  # List[Tuple[id, Mascota, id_dueno]]
    if not mascotas:
        print("No hay mascotas para actualizar.")
        return
    for i, (pet_id, mascota, owner_id) in enumerate(mascotas, start=1):
        print(f"{i}. ID {pet_id} | {mascota}")
    idx = input_int("Seleccione mascota (número): ", 1, len(mascotas)) - 1
    pet_id, _, old_owner_id = mascotas[idx]

    # Mostrar dueños para posible reasignación
    duenos = listar_duenos()
    for j, (owner_id, dueno) in enumerate(duenos, start=1):
        print(f"{j}. ID {owner_id} | {dueno}")
    d_idx = input_int("Seleccione nuevo dueño (número): ", 1, len(duenos)) - 1
    new_owner_id, _ = duenos[d_idx]

    # Pedir nuevos datos
    nombre = input("Nuevo nombre de la mascota: ").strip()
    especie = input("Nueva especie: ").strip()
    raza = input("Nueva raza: ").strip()
    edad = input_int("Nueva edad (años): ", 0)

    nueva = Mascota(nombre, especie, raza, edad, duenos[d_idx][1])
    try:
        actualizar_mascota(pet_id, nueva, new_owner_id)
        print(f"Mascota {pet_id} actualizada correctamente.")
    except Exception as e:
        print(f"Error al actualizar mascota: {e}")


def eliminar_mascota_db() -> None:
    print("\n-- Eliminar mascota (SQLite) --")
    mascotas = db_listar_mascotas()
    if not mascotas:
        print("No hay mascotas para eliminar.")
        return
    for i, (pet_id, mascota, _) in enumerate(mascotas, start=1):
        print(f"{i}. ID {pet_id} | {mascota}")
    idx = input_int("Seleccione mascota (número): ", 1, len(mascotas)) - 1
    pet_id, _, _ = mascotas[idx]

    confirm = input(f"¿Seguro que deseas eliminar la mascota {pet_id}? (s/n): ").lower()
    if confirm == 's':
        try:
            eliminar_mascota(pet_id)
            print(f"Mascota {pet_id} eliminada.")
        except Exception as e:
            print(f"Error al eliminar mascota: {e}")


# --------------------------------------------------
# Funciones para operaciones con Consultas
# --------------------------------------------------
def registrar_consulta_db() -> None:
    print("\n-- Registrar consulta (SQLite) --")
    try:
        mascotas = db_listar_mascotas()
        if not mascotas:
            print("Primero debe registrar una mascota.")
            return
        for i, m in enumerate(mascotas, start=1): print(f"{i}. {m}")
        idx = input_int("Seleccione mascota (número): ", 1, len(mascotas)) - 1
        selected = mascotas[idx]
        motivo = input("Motivo: ").strip()
        diagnostico = input("Diagnóstico: ").strip()
        consulta = Consulta(datetime.now(), motivo, diagnostico, selected)
        cons_id = db_agregar_consulta(consulta, idx+1)
        print(f"Consulta insertada en DB con id {cons_id}")
        logging.info(f"Consulta registrada en DB con id {cons_id}")
    except Exception as e:
        print(f"Error al insertar consulta en DB: {e}")
        logging.error(f"Error registrar_consulta_db: {e}")


def listar_consultas_db() -> None:
    print("\n-- Consultas registradas (SQLite) --")
    consultas = db_listar_consultas()
    if not consultas:
        print("No hay consultas registradas.")
        return
    for i, c in enumerate(consultas, start=1): print(f"{i}. {c}")


def actualizar_consulta_db() -> None:
    print("\n-- Actualizar consulta (SQLite) --")
    consultas = db_listar_consultas()  # List[Tuple[id, Consulta, id_mascota]]
    if not consultas:
        print("No hay consultas para actualizar.")
        return
    for i, (cons_id, consulta, _) in enumerate(consultas, start=1):
        print(f"{i}. ID {cons_id} | {consulta}")
    idx = input_int("Seleccione consulta (número): ", 1, len(consultas)) - 1
    cons_id, _, old_pet_id = consultas[idx]

    # Mostrar mascotas para reasignación
    mascotas = db_listar_mascotas()
    for j, (pet_id, mascota, _) in enumerate(mascotas, start=1):
        print(f"{j}. ID {pet_id} | {mascota}")
    m_idx = input_int("Seleccione nueva mascota (número): ", 1, len(mascotas)) - 1
    new_pet_id, new_pet, _ = mascotas[m_idx]

    # Pedir nuevos datos
    motivo = input("Nuevo motivo: ").strip()
    diagnostico = input("Nuevo diagnóstico: ").strip()
    fecha = datetime.now()  # o pedir fecha al usuario

    nueva = Consulta(fecha, motivo, diagnostico, new_pet)
    try:
        actualizar_consulta(cons_id, nueva, new_pet_id)
        print(f"Consulta {cons_id} actualizada correctamente.")
    except Exception as e:
        print(f"Error al actualizar consulta: {e}")


def eliminar_consulta_db() -> None:
    print("\n-- Eliminar consulta (SQLite) --")
    consultas = db_listar_consultas()
    if not consultas:
        print("No hay consultas para eliminar.")
        return
    for i, (cons_id, consulta, _) in enumerate(consultas, start=1):
        print(f"{i}. ID {cons_id} | {consulta}")
    idx = input_int("Seleccione consulta (número): ", 1, len(consultas)) - 1
    cons_id, _, _ = consultas[idx]

    confirm = input(f"¿Seguro que deseas eliminar la consulta {cons_id}? (s/n): ").lower()
    if confirm == 's':
        try:
            eliminar_consulta(cons_id)
            print(f"Consulta {cons_id} eliminada.")
        except Exception as e:
            print(f"Error al eliminar consulta: {e}")


# --------------------------------------------------
# Funciones para opciones de gestión en memoria
# --------------------------------------------------
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


# --------------------------------------------------
# Funciones de import/export
# --------------------------------------------------
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
    # Datos de memoria
    mascotas: List[Mascota] = []
    consultas: List[Consulta] = []
    try:
        # Intentar cargar de CSV/JSON
        mascotas, consultas = importar_datos()
    except:
        pass

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
                registrar_dueno_db()
            elif opcion == "8":
                listar_duenos_db()
            elif opcion == "9":
                actualizar_dueno_db()
            elif opcion == "10":
                eliminar_dueno_db()
            elif opcion == "11":
                registrar_mascota_db()
            elif opcion == "12":
                listar_mascotas_db()
            elif opcion == "13":
                actualizar_mascota_db()
            elif opcion == "14":
                eliminar_mascota_db()
            elif opcion == "15":
                registrar_consulta_db()
            elif opcion == "16":
                listar_consultas_db()
            elif opcion == "17":
                actualizar_consulta_db()
            elif opcion == "18":
                eliminar_consulta_db()
            elif opcion == "19":
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
