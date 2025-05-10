"""
Gestor de Correos Electrónicos - Biblioteca Universidad Tecnológica del Valle
Autores: Jonathan Cardona Calderon - Sandra Liliana Zapata Gallón
"""

# Colección para almacenar los correos registrados
correos_registrados = []

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar un nuevo correo electrónico")
    print("2. Ver correos registrados")
    print("3. Buscar un correo específico")
    print("4. Salir de la aplicación")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            print("Funcionalidad de registro aún no implementada.")
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
