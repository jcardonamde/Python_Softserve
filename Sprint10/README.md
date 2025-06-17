# :dog: Clínica Veterinaria Amigos Peludos — Prototipo Web Django (MVT)

Este proyecto es un primer prototipo de interfaz web para la Clínica Veterinaria "Amigos Peludos" desarrollado con Django siguiendo el patrón MVT (Modelo‑Vista‑Plantilla). Está pensado como una demo estática sin acceso a base de datos ni funcionalidades avanzadas.



---

## 📌 Estructura del Proyecto
:clipboard: models.py # Clases Dueno, Mascota, Consulta
:clipboard: storage.py # Funciones de serialización/deserialización (CSV y JSON)
:clipboard: utils.py # Funciones auxiliares (input_int, etc.)
:clipboard: app.py # Lógica principal: menú, bucle y llamadas a models/storage/utils
:clipboard: test_veterinaria.py # Pruebas unitarias con unittest
:open_file_folder: pycache/ # Cache automático de Python


## 📌 Características

* **Programación Orientada a Objetos**: Clases `Dueno`, `Mascota` y `Consulta`.

* **Registro de datos**:
  * Dueños y mascotas con datos básicos.
  * Registro de consultas veterinarias.

---

## 🚀 Requisitos

* Python 3.7 o superior.
* pip (gestor de paquetes de Python).

---

## ⚙️ Instrucciones de uso

1. Abre una terminal y sitúate en esta carpeta:

   ```bash
   git clone <URL_del_proyecto>
   cd Python_Softserve/Python_Softserve/Sprint10
   ```

2. Crea y activa un entorno virtual:

   ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
   ```

3. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplica migraciones (tablas Django por defecto, aunque no se usan modelos propios):
   ```bash
   python manage.py migrate
   ```

5. Arranca el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

6. Visita en tu navegador:

   * http://127.0.0.1:8000/  → Página de bienvenida
   * http://127.0.0.1:8000/services/  → Servicios veterinarios
   * http://127.0.0.1:8000/placeholder/  → Placeholder dinámico

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

  o abrirlo en un gestor de bases de datos como DBeaver.
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
