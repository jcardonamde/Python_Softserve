# :dog: Clínica Veterinaria Amigos Peludos

**Sistema Completo de Gestión para Veterinaria en Python**

Esta aplicación de consola en Python gestiona la información de una clínica veterinaria (dueños, mascotas y consultas), maneja logs, con persistencia en CSV/JSON, con pruebas unitarias organizadas con `unittest`, y ahora con persistencia de datos con SQLite para operaciones CRUD.

---

## 📌 Estructura del Proyecto
* :clipboard: models.py # Clases Dueno, Mascota, Consulta
* :clipboard: storage.py # Funciones de serialización/deserialización (CSV y JSON)
* :clipboard: utils.py # Funciones auxiliares (input_int, etc.)
* :clipboard: app.py # Lógica principal: menú, bucle y llamadas a models/storage/utils/database
* :clipboard: test_veterinaria.py # Pruebas unitarias con unittest
* :clipboard: database.py # Funciones para crear tablas y realizar operaciones CRUD con SQLite.
* :open_file_folder: pycache/ # Cache automático de Python


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
  * Registro, listado, actualización y eliminación en memoria y SQLite.

* **Gestión de Archivos Dinámica**:
  * Detecta la ruta del script (BASE_DIR) donde se ejecuta el script.
  * Crea y lee los archivos (`CSV`, `JSON`, `log`) en esa misma carpeta (Sprint8).

* **Pruebas Unitarias**:
  * Cobertura de modelos (`Dueno`, `Mascota`, `Consulta`) y sus métodos `__str__`.
  * Validación de serialización y deserialización a CSV/JSON.
  * Verificación de `input_int` para rangos y reintentos.
  * Asegura que el sistema de logging registre eventos críticos sin fallos.

* **Almacenamiento Híbrido**
  * **Memoria**: listados temporales en tiempo de ejecución.
  * **Archivos** (CSV/JSON): función de exportación e importación (`storage.py`).
  * **SQLite**: base de datos (`database.py`) con tablas para `duenos`, `mascotas` y `consultas`.

* **CRUD Completo en SQLite**
  - **Crear**: `agregar` para dueños, mascotas y consultas.
  - **Leer**: `listar` que devuelven tuplas `(id, objeto, [id_relacion])`.
  - **Actualizar**: `actualizar` por `id`.
  - **Eliminar**: `eliminar` por `id`.


---

## 🚀 Requisitos

* Python 3.7 o superior.
* No requiere dependencias externas más allá de la biblioteca estándar (usa módulos csv, json, logging, os, datetime, unittest, sqlite3).

*Desarrollado con buenas prácticas de POO en Python.*

---

## ⚙️ Instrucciones de uso

1. Clona o descarga este repositorio:

   ```bash
   git clone <URL_del_proyecto>
   cd Sprint8
   ```

2. Asegúrate de tener Python 3.7+ instalado:

   ```bash
   python --version
   ```

3. Ejecuta la aplicación principal:

   ```bash
   python app.py
   ```

4. Verás el menú con opciones para:

   - Registrar/listar/actualizar/eliminar dueños, mascotas y consultas en SQLite.
   - Registrar/listar en memoria y exportar/importar en CSV/JSON.
   - Salir (con guardado automático de CSV/JSON).

5. Para ejecutar las pruebas unitarias, en la misma carpeta:

   ```bash
   python -m unittest test_veterinaria.py
   ```

O bien, para que descubra todos los tests automáticamente:

   ```bash
   python -m unittest discover -v
   ```
---

## 🗄️ Base de Datos SQLite

* Archivo generado: `clinica_veterinaria.db` en la carpeta del proyecto.
* Para inspeccionarlo, puedes usar el cliente `sqlite3`:
  ```bash
  sqlite3 clinica_veterinaria.db
  .tables
  .schema duenos
  .schema mascotas
  .schema consultas
  .exit
  ```

  o puede explorarlo en un gestor de bases de datos como DBeaver.
---

## 📄 Archivos Generados

* `clinica_veterinaria.db` — Base de datos SQLite.
* `mascotas_dueños.csv` & `consultas.json` — Exportaciones en CSV/JSON.
* `clinica_veterinaria.log` — Registro de eventos.

---

## 📄 Licencia
Este proyecto ha sido desarrollado con fines académicos para el Bootcamp de Python Softserve. 
Puedes usar, modificar y distribuir libremente este código para fines educativos o personales.
No se permite su uso con fines comerciales sin autorización.
