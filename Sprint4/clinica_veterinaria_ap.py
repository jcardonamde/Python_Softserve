"""
Ejercicio Sprint4: Sistema Simple de Gestión para Veterinaria 

Sistema de atención a mascotas y gestión administrativa - Clínica Veterinaria "Amigos Peludos"
Autores: Jonathan Cardona Calderon - Sandra Liliana Zapata Gallón
"""

from datetime import datetime
from typing import List
import sys

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


# --- Funciones de gestión ---
def input_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    Solicita un entero al usuario, validando rango opcional.
    """
    while True:
        try:
            valor = int(input(prompt).strip())
            if min_val is not None and valor < min_val:
                print(f"Por favor ingrese un valor >= {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f"Por favor ingrese un valor <= {max_val}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")


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
    """
    print("\n-- Registrar nueva mascota --")
    nombre = input("Nombre de la mascota: ").strip()
    especie = input("Especie: ").strip()
    raza = input("Raza: ").strip()
    edad = int(input("Edad (años): ").strip())

    print("\nDatos del dueño:")
    nombre_d = input("  Nombre: ").strip()
    tel = input("  Teléfono: ").strip()
    dir = input("  Dirección: ").strip()

    dueno = Dueno(nombre_d, tel, dir)
    mascota = Mascota(nombre, especie, raza, edad, dueno)
    mascotas.append(mascota)
    print(f"\n Mascota '{nombre}' registrada correctamente.")


def listar_mascotas(mascotas: List[Mascota]) -> None:
    """
    Muestra todas las mascotas registradas.
    """
    print("\n-- Mascotas registradas --")
    if not mascotas:
        print("No hay mascotas registradas.")
        return
    for i, m in enumerate(mascotas, start=1):
        print(f"{i}. {m}")


def registrar_consulta(mascotas: List[Mascota], consultas: List[Consulta]) -> None:
    """
    Registra una consulta para una mascota existente.
    """
    print("\n-- Registrar consulta veterinaria --")
    if not mascotas:
        print("Antes debe registrar al menos una mascota.")
        return

    listar_mascotas(mascotas)
    idx = int(input("Seleccione el número de la mascota: ").strip()) - 1
    if idx not in range(len(mascotas)):
        print("Selección inválida.")
        return

    motivo = input("Motivo de la consulta: ").strip()
    diagnostico = input("Diagnóstico: ").strip()
    fecha = datetime.now()

    consulta = Consulta(fecha, motivo, diagnostico, mascotas[idx])
    consultas.append(consulta)
    print(f"\n Consulta registrada para '{mascotas[idx].nombre}'.")


def ver_historial(mascotas: List[Mascota], consultas: List[Consulta]) -> None:
    """
    Muestra el historial de consultas de una mascota específica.
    """
    print("\n-- Historial de consultas --")
    if not mascotas:
        print("No hay mascotas registradas.")
        return

    listar_mascotas(mascotas)
    idx = int(input("Seleccione el número de la mascota: ").strip()) - 1
    if idx not in range(len(mascotas)):
        print("Selección inválida.")
        return

    pet = mascotas[idx]
    historial = [c for c in consultas if c.mascota is pet]
    if not historial:
        print(f"No hay consultas registradas para '{pet.nombre}'.")
    else:
        print(f"\nConsultas de '{pet.nombre}':")
        for c in historial:
            print(c)


# --- Bucle principal con manejo de interrupción ---
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
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida, intente de nuevo.")
    except KeyboardInterrupt:
        print("\nInterrupción recibida. Saliendo...")
        sys.exit(0)


# --- Ejecución del programa ---
if __name__ == "__main__":
    main()