# :dog: Clínica Veterinaria Amigos Peludos — Prototipo Web Django (MVT) con Persistencia con Django ORM

En esta versión hemos integrado la capa de persistencia usando el ORM de Django. Definimos dos modelos principales: Propietario (nombre, teléfono, email) y Mascota (nombre, especie, edad, propietario).

Registramos ambos modelos en el panel de administración de Django para gestión rápida. Creamos migraciones y generamos la base de datos SQLite automáticamente. Desarrollamos vistas y plantillas (listado y formulario) basadas en ModelForm para registrar y listar propietarios y mascotas.

---


## 🚀 Requisitos

* Python 3.7 o superior.
* pip (gestor de paquetes de Python).

---

## ⚙️ Instrucciones de uso

1. Abre una terminal y sitúate en esta carpeta:

   ```bash
   git clone <URL_del_proyecto>
   cd Python_Softserve/Python_Softserve/Sprint10_11
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

4. Aplica migraciones (tablas Django por defecto, aunque no se usan modelos propios):
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


8. 👀 Previews ORM:
![](https://docs.google.com/drawings/d/e/2PACX-1vSBztgBwd3GoxGSQA-oHlHcSQhDhviGZ13yeOL1g0J7Dir_3UrzuPj095orL42VEbaKnhOIUjQrydIk/pub?w=960&h=720)

![](https://docs.google.com/drawings/d/e/2PACX-1vTkpl4WFk4q-rQPw1LerB6HRvOAllnNeEr3BWLH5rEAt-vpS1zuDywVq8TcW3PLFcl-irN75iNZVzgr/pub?w=960&h=720)


---

📂 Estructura de Carpetas

    ```bash
    Sprint10_11/
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

---

## 🎨 Diseño y Estilos

* CSS básico en static/css/style.css.
* Para agregar más estilos, modifica ese archivo o crea nuevas carpetas bajo static/.

---

## 📄 Licencia
Proyecto académico para la digitalización de la Clínica Veterinaria “Amigos Peludos”. Uso y modificación permitidos con fines educativos o de demostración. No comercial sin autorización.
