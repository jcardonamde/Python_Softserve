"""
Ejercicio Sprint4: Sistema Simple de Gestión para Veterinaria 

Sistema de atención a mascotas y gestión administrativa - Clínica Veterinaria "Amigos Peludos"
Autores: Jonathan Cardona Calderon - Sandra Liliana Zapata Gallón
"""

from datetime import datetime

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

