"""
Ejercicio Sprint5: Sistema Avanzado de Gestión para Veterinaria con Manejo de Excepciones y Logging

Sistema de atención a mascotas y gestión administrativa - Clínica Veterinaria "Amigos Peludos"
Autores: Jonathan Cardona Calderon - Sandra Liliana Zapata Gallón
"""

from datetime import datetime
from typing import List
import sys
import logging


# Configurar logging
logging.basicConfig(
    filename='clinica_veterinaria.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.info('Inicio de la aplicación')


# --- Clases para representar entidades ---
class Dueno:
    """
    Representa al dueño de una mascota.
    Atributos:
        nombre (str): Nombre completo del dueño.
        telefono (str): Número de contacto.
        direccion (str): Dirección postal.
    """
    def __init__(self, nombre: str, telefono: str, direccion: str) -> None:
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self) -> str:
        return f"Dueño: {self.nombre} | Tel: {self.telefono} | Dir: {self.direccion}"


class Mascota:
    """
    Representa a una mascota registrada en la clínica.
    Atributos:
        nombre (str): Nombre de la mascota.
        especie (str): Especie (perro, gato, etc.).
        raza (str): Raza de la mascota.
        edad (int): Edad en años completos.
        dueno (Dueno): Instancia de la clase Dueno asociada.
    """
    def __init__(self, nombre: str, especie: str, raza: str, edad: int, dueno: Dueno) -> None:
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueno = dueno

    def __str__(self) -> str:
        return (f"Mascota: {self.nombre} | Especie: {self.especie} | Raza: {self.raza} | "
                f"Edad: {self.edad} años\n  {self.dueno}")


class Consulta:
    """
    Representa una consulta veterinaria de una mascota.
    Atributos:
        fecha (datetime): Fecha y hora de la consulta.
        motivo (str): Motivo de la consulta (síntomas, chequeo, etc.).
        diagnostico (str): Diagnóstico dado por el veterinario.
        mascota (Mascota): Instancia de la mascota consultada.
    """
    def __init__(self, fecha: datetime, motivo: str, diagnostico: str, mascota: Mascota) -> None:
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota

    def __str__(self) -> str:
        fecha_str = self.fecha.strftime("%Y-%m-%d %H:%M")
        return (f"[{fecha_str}] Consulta de '{self.mascota.nombre}': Motivo: {self.motivo} | "
                f"Diagnóstico: {self.diagnostico}")


# --- Función auxiliar para validar enteros con logging ---
def input_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    Solicita un entero al usuario, validando rango opcional.
    Registra advertencias en el log si la entrada es inválida
    """
    while True:
        try:
            valor = int(input(prompt).strip())
            if min_val is not None and valor < min_val:
                msg = f"Valor {valor} menor que mínimo {min_val}."
                print(msg)
                logging.warning(f"Entrada fuera de rango: {msg}")
                continue
            if max_val is not None and valor > max_val:
                msg = f"Valor {valor} mayor que máximo {max_val}."
                print(msg)
                logging.warning(f"Entrada fuera de rango: {msg}")
                continue
            return valor
        except ValueError:
            msg = "No ingresó un número entero válido."
            print(msg)
            logging.warning(f"Entrada inválida: {msg}")


# --- Funciones del menú con manejo de excepciones --
def mostrar_menu() -> str:
    print("\n=== Clínica Veterinaria Amigos Peludos ===")
    print("1. Registrar mascota")
    print("2. Registrar consulta")
    print("3. Listar mascotas")
    print("4. Ver historial de consultas")
    print("5. Salir")
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


# --- Bucle principal con manejo manejo global de excepciones ---
def main() -> None:
    mascotas: List[Mascota] = []
    consultas: List[Consulta] = []

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
                msg = "Saliendo del programa..."
                print("¡Hasta luego!")
                logging.info(msg)
                break
            else:
                print("Opción no válida, intente de nuevo.")
                logging.warning(f"Opción inválida en menú: {opcion}")
    except KeyboardInterrupt:
        print("\nInterrupción recibida. Saliendo...")
        logging.info("Interrupción del programa por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"Error inesperado: {e}")
        logging.error(f"Excepción no controlada en el bucle principal: {e}")
        sys.exit(1)


# --- Ejecución del programa ---
if __name__ == "__main__":
    main()