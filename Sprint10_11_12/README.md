# :dog: Clínica Veterinaria Amigos Peludos — Interfaz Web con Django (MVT) con Persistencia con Django ORM

En esta versión hemos integrado la capa de persistencia usando el ORM de Django. Se tienen definidos los modelos principales: 
* Propietario (nombre, teléfono, email).
* Mascota (nombre, especie, edad, propietario).
* Citas (mascota, fecha, motivo, diagnostico).

Manejo de Módulos independientes. Registramos los modelos en el panel de administración de Django para gestión rápida. Migraciones y panel de administración activado. Desarrollamos vistas y plantillas dinámicas con Boostrap para registrar y listar dueños, mascotas y citas. Entorno virtual gestionado y dependencias en requirements.txt.

---


## 🚀 Requisitos

* Python 3.7 o superior.
* pip (gestor de paquetes de Python).

---

## ⚙️ Instrucciones de uso

1. Abre una terminal y sitúate en esta carpeta:

   ```bash
   git clone <URL_del_proyecto>
   cd Python_Softserve/Python_Softserve/Sprint10_11_12
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

   Si tu requirements.txt cambió, vuelve a congelarlo:
   ```bash
   pip install django
   pip freeze > requirements.txt
   ```

4. Aplica migraciones para modelos del aplicativo:
   ```bash
   python manage.py makemigrations clinic
   python manage.py migrate
   ```

5. Registro de superusuario
   ```bash
   python manage.py createsuperuser
   ```

6. Arranca el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

7. Visita en tu navegador:

   * http://127.0.0.1:8000/  → Página de bienvenida
   * http://127.0.0.1:8000/services/  → Servicios veterinarios
   * http://127.0.0.1:8000/placeholder/  → Placeholder dinámico
   * http://127.0.0.1:8000/owners/      → Listado de propietarios
   * http://127.0.0.1:8000/owners/new/  → Crear propietario
   * http://127.0.0.1:8000/pets/        → Listado de mascotas
   * http://127.0.0.1:8000/pets/new/    → Crear mascota
   * http://127.0.0.1:8000/appointments/ → Listado de citas
   * http://127.0.0.1:8000/appointments/new/ → Crear citas


8. 👀 Previews ORM:
![](https://docs.google.com/drawings/d/e/2PACX-1vSBztgBwd3GoxGSQA-oHlHcSQhDhviGZ13yeOL1g0J7Dir_3UrzuPj095orL42VEbaKnhOIUjQrydIk/pub?w=960&h=720)

![](https://docs.google.com/drawings/d/e/2PACX-1vTkpl4WFk4q-rQPw1LerB6HRvOAllnNeEr3BWLH5rEAt-vpS1zuDywVq8TcW3PLFcl-irN75iNZVzgr/pub?w=960&h=720)

![](https://docs.google.com/drawings/d/e/2PACX-1vSAcs43aEe2eOSqqBqkTOLP7en1yOIGIDaj7-TbJzyYDOOVnC-rzgK7uemcsa5KAoFMVls9ItqszgQA/pub?w=960&h=720)
---

📂 Estructura de Carpetas

    ```bash
    Sprint10_11_12/
    ├── clinic/             # App Django: views, urls y tests básicos
    │   ├── migrations/     # Migraciones para crear las tablas
    │   ├── templates/      # Plantillas HTML para cada vista
    │   │   └── clinic/
    │   │       ├── home.html
    │   │       ├── services.html
    │   │       └── placeholder.html
    │   │       └── mascota_form.html
    │   │       └── mascota_list.html
    │   │       └── propietario_form.html
    │   │       └── propietario_list.html
    │   │       └── cita_form.html
    │   │       └── cita_list.html
    │   │   └── base.html
    │   │ 
    │   ├── urls.py         # Rutas de la app
    │   └── views.py        # Lógica de renderizado
    │   └── forms.py        # Formulario para los modelos
    │   └── models.py       # Modelos para el ORM
    │
    ├── veterinary/         # Proyecto Django
    │   ├── settings.py     # Configuración (INSTALLED_APPS, templates, static)
    │   ├── urls.py         # Inclusión de `clinic.urls`
    │   └── wsgi.py
    │
    ├── static/             # Archivos estáticos (CSS, imágenes opcionales)
    │   └── imgs/
    │   └── css/
    │       └── style.css
    │
    ├── manage.py           # CLI de Django
    ├── requirements.txt    # Dependencias (Django)
    ├── venv/               # Entorno virtual (ignorado por Git)
    └── .gitignore          # Ignora venv/, __pycache__/, db.sqlite3, etc.
    ```

---

## 📄 .gitignore

* Asegúrate de ignorar:

   ```bash
    venv/
    __pycache__/
    db.sqlite3
    *.pyc
    /staticfiles/
   ```

---

## 📝 Descripción de Rutas

| URL          | Vista       | Template                |
|--------------|-------------|-------------------------|
| /            | home        | clinic/home.html        |
| /services/   | services    | clinic/services.html    |
| /placeholder/| placeholder | clinic/placeholder.html |
| /owners/     | propietario_list | clinic/propietario_list.html |
| /owners/new/ | propietario_create | clinic/propietario_form.html |
| /pets/       | mascota_list | clinic/mascota_list.html |
| /pets/new/   | mascota_create | clinic/mascota_form.html |
| /appointments/     | cita_list | clinic/cita_list.html |
| /appointments/new/ | cita_create | clinic/cita_form.html |

---

## 🎨 Diseño y Estilos

* CSS básico en static/css/style.css.
* Para agregar más estilos, modifica ese archivo o crea nuevas carpetas bajo static/.
* Importación de libreria Bootstrap CDN
* Importación de libreria Font Awesone CDN

---

## 📄 Licencia
Proyecto académico para la digitalización de la Clínica Veterinaria “Amigos Peludos”. Uso y modificación permitidos con fines educativos o de demostración. No comercial sin autorización.
