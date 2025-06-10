# :dog: Clínica Veterinaria Amigos Peludos

**Sistema Completo de Gestión para Veterinaria en Python**

Esta aplicación de consola en Python gestiona la información de una clínica veterinaria (dueños, mascotas y consultas), maneja logs, con persistencia en CSV/JSON y ahora con pruebas unitarias organizadas con `unittest`.

---

## 📌 Estructura del Proyecto
- :clipboard: models.py # Clases Dueno, Mascota, Consulta
- :clipboard: storage.py # Funciones de serialización/deserialización (CSV y JSON)
- :clipboard: utils.py # Funciones auxiliares (input_int, etc.)
- :clipboard: app.py # Lógica principal: menú, bucle y llamadas a models/storage/utils
- :clipboard: test_veterinaria.py # Pruebas unitarias con unittest
- :open_file_folder: pycache/ # Cache automático de Python

<br>

## 📌 Características

* **Programación Orientada a Objetos**: Clases `Dueno`, `Mascota` y `Consulta`.

* **Registro de datos**:
  * Dueños y mascotas con datos básicos.
  * Registro de consultas veterinarias.

* **Listados**:
  * Ver todas las mascotas registradas.
  * Mostrar historial de consultas por mascota.

* **Validaciones**:
  * Verificación de entradas numéricas (edad, selección de índices).
  * Manejo de interrupción (Ctrl+C) para salir de forma segura.

* **Robustez y monitoreo**:
  * Manejo estructurado de excepciones (try-except) para entradas inválidas y errores de flujo.
  * Sistema de logging con logging para registrar eventos INFO, WARNING y ERROR en clinica_veterinaria.log, dentro de la carpeta del script.

* **Persistencia de Datos**:
  * Exportación a mascotas_dueños.csv (CSV) y consultas.json (JSON).
  * Importación automática de datos al iniciar la aplicación.
  * Guardado de datos al finalizar y opciones manuales en el menú.

* **Gestión de Archivos Dinámica**:
  * Detecta la ruta del script (BASE_DIR) donde se ejecuta el script.
  * Crea y lee los archivos (`CSV`, `JSON`, `log`) en esa misma carpeta (Sprint7).

* **Pruebas Unitarias**:
  * Cobertura de modelos (`Dueno`, `Mascota`, `Consulta`) y sus métodos `__str__`.
  * Validación de serialización y deserialización a CSV/JSON.
  * Verificación de `input_int` para rangos y reintentos.
  * Asegura que el sistema de logging registre eventos críticos sin fallos.

---

## 🚀 Requisitos

* Python 3.7 o superior.
* No requiere dependencias externas más allá de la biblioteca estándar (usa módulos csv, json, logging, os, datetime, unittest).

*Desarrollado con buenas prácticas de POO en Python.*

---

## ⚙️ Instrucciones de uso

1. Clona o descarga este repositorio:

   ```bash
   git clone <URL_del_proyecto>
   cd Sprint7
   ```

2. Asegúrate de tener Python 3.7+ instalado:

   ```bash
   python --version
   ```

3. Ejecuta la aplicación principal:

   ```bash
   python app.py
   ```

4. Sigue el menú en consola para:

   * Registrar mascota
   * Registrar consulta
   * Listar mascotas
   * Ver historial de consultas
   * Exportar datos (CSV/JSON)
   * Importar datos (CSV/JSON)
   * Salir

5. Para ejecutar las pruebas unitarias, en la misma carpeta:

   ```bash
   python -m unittest test_veterinaria.py
   ```

O bien, para que descubra todos los tests automáticamente:

   ```bash
   python -m unittest discover -v
   ```
---

## 📄 Archivos Generados

* clinica_veterinaria.log — registro de eventos de la aplicación (en la misma carpeta).
* mascotas_dueños.csv — lista de mascotas y sus dueños.
* consultas.json — historial de consultas veterinarias.

---

## 📄 Licencia
Este proyecto ha sido desarrollado con fines académicos para el Bootcamp de Python Softserve. 
Puedes usar, modificar y distribuir libremente este código para fines educativos o personales.
No se permite su uso con fines comerciales sin autorización.
