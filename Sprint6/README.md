# :dog: Clínica Veterinaria Amigos Peludos

**Sistema de Gestión Avanzado Veterinaria en Python**

Esta versión amplía la aplicación de consola incorporando serialización y deserialización de datos en CSV (mascotas y dueños) y JSON (consultas), además de ubicar automáticamente todos los archivos generados junto al script.

---

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
  * Detecta la ruta del script (BASE_DIR) y crea/lee los archivos en esa misma carpeta (Sprint6).

---

## 🚀 Requisitos

* Python 3.7 o superior.
* No requiere dependencias externas más allá de la biblioteca estándar (usa módulos csv, json, logging, os, datetime).

*Desarrollado con buenas prácticas de POO en Python.*

---

## ⚙️ Instrucciones de uso

1. Clona o descarga este repositorio:

   ```bash
   git clone <URL_del_proyecto>
   cd Sprint6
   ```

2. Asegúrate de tener Python 3.7+ instalado:

   ```bash
   python --version
   ```

3. Ejecuta la aplicación:

   ```bash
   python clinica_veterinaria_file.py
   ```

4. Sigue el menú en consola para:

   * Registrar mascota
   * Registrar consulta
   * Listar mascotas
   * Ver historial de consultas
   * Exportar datos (CSV/JSON)
   * Importar datos (CSV/JSON)
   * Salir

---

## 📄 Archivos Generados

* mascotas_dueños.csv — lista de mascotas y sus dueños.
* consultas.json — historial de consultas veterinarias.
* clinica_veterinaria.log — registro de eventos de la aplicación.

---

## 📄 Licencia
Este proyecto ha sido desarrollado con fines académicos para el Bootcamp de Python Softserve. 
Puedes usar, modificar y distribuir libremente este código para fines educativos o personales.
No se permite su uso con fines comerciales sin autorización.
