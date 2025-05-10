"""
Gestor de Correos Electrónicos - Biblioteca Universidad Tecnológica del Valle
Autores: Jonathan Cardona Calderon - Sandra Liliana Zapata Gallón
"""

import re

# Colección para almacenar correos como diccionarios
correos_registrados = []

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar un nuevo correo electrónico")
    print("2. Ver correos registrados")
    print("3. Buscar un correo específico")
    print("4. Salir de la aplicación")

def validar_correo(correo: str) -> str | None:
    """
    Valida el correo usando regex y clasifica como estudiante o docente.
    Retorna el tipo si es válido, None si es inválido.
    """
    patron = r'^[\w\.-]+@(?:estudiante\.utv\.edu\.co|utv\.edu\.co)$'
    if re.match(patron, correo):
        if correo.endswith("@estudiante.utv.edu.co"):
            return "estudiante"
        elif correo.endswith("@utv.edu.co"):
            return "docente"
    return None

def registrar_correo():
    correo = input("Ingrese el correo electrónico: ").strip().lower()
    tipo = validar_correo(correo)

    if tipo:
        correos_registrados.append({"correo": correo, "tipo": tipo})
        print(f"Correo registrado exitosamente como {tipo}.")
    else:
        print("Correo no válido. Verifique el formato y dominio.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            registrar_correo()
        elif opcion == "2":
            print("Funcionalidad de visualización aún no implementada.")
        elif opcion == "3":
            print("Funcionalidad de búsqueda aún no implementada.")
        elif opcion == "4":
            print("Gracias por usar el gestor de correos. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
