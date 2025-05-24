# :dog: Clínica Veterinaria Amigos Peludos

**Sistema de Gestión Veterinaria en Python**

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar la información de una clínica veterinaria: dueños, mascotas y consultas.

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

---

## 🚀 Requisitos Técnicos

* Python 3.7 o superior.
* No requiere dependencias externas más allá de la biblioteca estándar.

---

## 🎯 Requisitos Funcionales

- Registrar nuevas mascotas y asignarlas a un dueño con datos completos (nombre, especie, raza, edad, teléfono y dirección del dueño).
- Registrar consultas veterinarias para una mascota específica con fecha y hora automáticas, motivo y diagnóstico.
- Listar todas las mascotas registradas, mostrando sus datos y los del dueño.
- Ver el historial de consultas de una mascota en particular, detallando fecha, motivo y diagnóstico.
- Salir de la aplicación de forma segura mediante la opción de menú o con Ctrl+C.

---

## 🧰 Tecnologías y Conceptos Usados

- **Python 3.7+** como lenguaje de programación.
- **Programación Orientada a Objetos (POO)** para modelar entidades.
- **Modularidad** y funciones independientes para cada funcionalidad.
- **Validación de entradas** con función auxiliar `input_int`.
- **Manejo de excepciones** y captura de `KeyboardInterrupt` para una salida controlada.
- **Biblioteca estándar**: `datetime`, `typing`, `sys`.

---

## ⚙️ Instrucciones de uso

1. Clona o descarga este repositorio:

   ```bash
   git clone <URL_del_proyecto>
   cd Sprint4
   ```

2. Asegúrate de tener Python 3.7+ instalado:

   ```bash
   python --version
   ```

3. Ejecuta la aplicación:

   ```bash
   python clinica_veterinaria_ap.py
   ```

4. Sigue el menú en consola para:

   * Registrar mascota
   * Registrar consulta
   * Listar mascotas
   * Ver historial de consultas
   * Salir

---

## 📄 Licencia
Este proyecto ha sido desarrollado con fines académicos para el Bootcamp de Python Softserve. 
Puedes usar, modificar y distribuir libremente este código para fines educativos o personales.
No se permite su uso con fines comerciales sin autorización.
