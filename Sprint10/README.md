# :dog: Clínica Veterinaria Amigos Peludos — Prototipo Web Django (MVT)

Este proyecto es un primer prototipo de interfaz web para la Clínica Veterinaria "Amigos Peludos" desarrollado con Django siguiendo el patrón MVT (Modelo‑Vista‑Plantilla). Está pensado como una demo estática sin acceso a base de datos ni funcionalidades avanzadas.

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

📂 Estructura de Carpetas

    ```bash
    Sprint10/
    ├── clinic/             # App Django: views, urls y tests básicos
    │   ├── templates/      # Plantillas HTML para cada vista
    │   │   └── clinic/
    │   │       ├── home.html
    │   │       ├── services.html
    │   │       └── placeholder.html
    │   ├── urls.py         # Rutas de la app
    │   └── views.py        # Lógica de renderizado
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

---

## 🎨 Diseño y Estilos

* CSS básico en static/css/style.css.
* Para agregar más estilos, modifica ese archivo o crea nuevas carpetas bajo static/.

---

## 📄 Licencia
Proyecto académico para la digitalización de la Clínica Veterinaria “Amigos Peludos”. Uso y modificación permitidos con fines educativos o de demostración. No comercial sin autorización.
