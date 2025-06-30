# 🏥 Clínica Veterinaria "Amigos Peludos" — Sistema Web Completo con Django

## 📋 Descripción del Proyecto

Sistema de gestión integral para clínica veterinaria desarrollado con Django 5.2.3, implementando el patrón MVT (Model-View-Template) con persistencia de datos mediante Django ORM. El proyecto incluye gestión completa de pacientes, citas, medicamentos, cirugías y bitácoras clínicas.

### ✨ Características Principales

- **Gestión de Propietarios**: Registro y administración de dueños de mascotas
- **Gestión de Mascotas**: Control de pacientes con historial completo
- **Sistema de Citas**: Programación y seguimiento de consultas veterinarias
- **Inventario de Medicamentos**: Control de stock y fechas de vencimiento
- **Programación de Cirugías**: Gestión de procedimientos quirúrgicos
- **Bitácoras Clínicas**: Registro detallado de observaciones y tratamientos
- **Historia Clínica**: Vista consolidada del historial médico de cada mascota
- **Exportación de Datos**: Funcionalidad para exportar información en formato CSV
- **Panel de Administración**: Interfaz de gestión avanzada con Django Admin

---

## 🚀 Requisitos del Sistema

- **Python**: 3.7 o superior
- **Django**: 5.2.3
- **Base de Datos**: SQLite3 (incluida)
- **Navegador Web**: Moderno con soporte para HTML5 y CSS3

---

## ⚙️ Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/jcardonamde/Python_Softserve.git
cd Python_Softserve/Sprint10_11_12_13
```

### 2. Crear y Activar Entorno Virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos
```bash
# Aplicar migraciones
python manage.py makemigrations clinic
python manage.py migrate
```

### 5. Crear Superusuario
```bash
python manage.py createsuperuser
# Usuario configurado: artemis
```

### 6. Ejecutar el Servidor
```bash
python manage.py runserver
```

---

## 🌐 Acceso a la Aplicación

### URLs Principales
| URL | Descripción | Funcionalidad |
|-----|-------------|---------------|
| `http://127.0.0.1:8000/` | Página de inicio | Bienvenida y navegación |
| `http://127.0.0.1:8000/services/` | Servicios veterinarios | Información de servicios |
| `http://127.0.0.1:8000/placeholder/` | Página de prueba | Placeholder dinámico |

### Gestión de Propietarios
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/owners/` | Listado de propietarios |
| `http://127.0.0.1:8000/owners/new/` | Crear nuevo propietario |

### Gestión de Mascotas
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/pets/` | Listado de mascotas |
| `http://127.0.0.1:8000/pets/new/` | Crear nueva mascota |

### Gestión de Citas
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/appointments/` | Listado de citas |
| `http://127.0.0.1:8000/appointments/new/` | Crear nueva cita |

### Gestión de Medicamentos
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/medicines/` | Listado de medicamentos |
| `http://127.0.0.1:8000/medicines/new/` | Crear medicamento |
| `http://127.0.0.1:8000/medicines/<id>/edit/` | Editar medicamento |
| `http://127.0.0.1:8000/medicines/<id>/delete/` | Eliminar medicamento |

### Gestión de Cirugías
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/surgeries/` | Listado de cirugías |
| `http://127.0.0.1:8000/surgeries/new/` | Programar cirugía |
| `http://127.0.0.1:8000/surgeries/<id>/edit/` | Editar cirugía |
| `http://127.0.0.1:8000/surgeries/<id>/delete/` | Cancelar cirugía |

### Gestión de Bitácoras
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/logs/` | Listado de bitácoras |
| `http://127.0.0.1:8000/logs/new/` | Crear bitácora |
| `http://127.0.0.1:8000/logs/<id>/edit/` | Editar bitácora |
| `http://127.0.0.1:8000/logs/<id>/delete/` | Eliminar bitácora |

### Historia Clínica
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/historia/` | Selector de mascotas |
| `http://127.0.0.1:8000/history/<mascota_id>/` | Historia clínica específica |

### Exportación de Datos
| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/export/owners/` | Exportar propietarios (CSV) |
| `http://127.0.0.1:8000/export/pets/` | Exportar mascotas (CSV) |

---

## 🗄️ Modelos de Datos

### Propietario
- **nombre**: Nombre completo del propietario
- **telefono**: Número de contacto
- **email**: Correo electrónico

### Mascota
- **nombre**: Nombre de la mascota
- **especie**: Tipo de animal (perro, gato, etc.)
- **edad**: Edad en años
- **propietario**: Relación con el propietario (ForeignKey)

### Cita
- **mascota**: Mascota atendida (ForeignKey)
- **fecha**: Fecha y hora de la cita
- **motivo**: Razón de la consulta
- **diagnostico**: Diagnóstico realizado (opcional)

### Medicamento
- **nombre**: Nombre del medicamento
- **descripcion**: Descripción detallada
- **cantidad**: Stock disponible
- **fecha_venc**: Fecha de vencimiento

### Cirugía
- **mascota**: Mascota a operar (ForeignKey)
- **veterinario**: Veterinario responsable
- **fecha_plan**: Fecha programada
- **descripcion**: Descripción del procedimiento

### Bitácora
- **cita**: Cita asociada (ForeignKey)
- **observacion**: Observaciones clínicas
- **tratamiento**: Tratamiento aplicado (opcional)
- **creada_en**: Timestamp de creación

---

## 📁 Estructura del Proyecto

```
Sprint10_11_12_13/
├── clinic/                     # Aplicación principal Django
│   ├── migrations/            # Migraciones de base de datos
│   ├── templates/             # Plantillas HTML
│   │   ├── base.html         # Plantilla base
│   │   ├── clinic/           # Plantillas principales
│   │   │   ├── home.html
│   │   │   ├── services.html
│   │   │   ├── placeholder.html
│   │   │   ├── mascota_form.html
│   │   │   ├── mascota_list.html
│   │   │   ├── propietario_form.html
│   │   │   ├── propietario_list.html
│   │   │   ├── cita_form.html
│   │   │   ├── cita_list.html
│   │   │   ├── historia_index.html
│   │   │   ├── historia_clinica.html
│   │   │   └── error.html
│   │   ├── medications/      # Plantillas de medicamentos
│   │   │   ├── medicamento_list.html
│   │   │   ├── medicamento_form.html
│   │   │   └── medicamento_confirm_delete.html
│   │   ├── surgeries/        # Plantillas de cirugías
│   │   │   ├── cirugia_list.html
│   │   │   ├── cirugia_form.html
│   │   │   └── cirugia_confirm_delete.html
│   │   └── logs/             # Plantillas de bitácoras
│   │       ├── bitacora_list.html
│   │       ├── bitacora_form.html
│   │       └── bitacora_confirm_delete.html
│   ├── admin.py              # Configuración del panel de administración
│   ├── apps.py               # Configuración de la aplicación
│   ├── forms.py              # Formularios Django
│   ├── models.py             # Modelos de datos
│   ├── urls.py               # Configuración de URLs
│   ├── utils.py              # Utilidades (exportación CSV)
│   ├── views.py              # Vistas y lógica de negocio
│   └── tests.py              # Pruebas unitarias
├── veterinary/               # Proyecto Django principal
│   ├── settings.py           # Configuración del proyecto
│   ├── urls.py               # URLs principales
│   ├── wsgi.py               # Configuración WSGI
│   └── asgi.py               # Configuración ASGI
├── static/                   # Archivos estáticos
│   ├── css/
│   │   └── style.css         # Estilos personalizados
│   └── imgs/
│       └── bg_perro_gato.jpg # Imágenes del proyecto
├── venv/                     # Entorno virtual (ignorado por Git)
├── clinic.log                # Archivo de logs de la aplicación
├── db.sqlite3                # Base de datos SQLite
├── manage.py                 # Script de gestión de Django
├── requirements.txt          # Dependencias del proyecto
├── instructions.txt          # Instrucciones rápidas
├── .gitignore                # Archivos ignorados por Git
└── README.md                 # Este archivo
```

---

## 🎨 Características de la Interfaz

### Diseño y Estilos
- **Bootstrap 5**: Framework CSS para diseño responsive
- **Font Awesome**: Iconografía moderna
- **CSS Personalizado**: Estilos específicos en `static/css/style.css`
- **Diseño Responsive**: Adaptable a diferentes tamaños de pantalla

### Funcionalidades de la UI
- **Navegación Intuitiva**: Menú de navegación claro y organizado
- **Formularios Validados**: Validación en frontend y backend
- **Tablas Interactivas**: Listados con paginación y filtros
- **Confirmaciones**: Diálogos de confirmación para acciones destructivas
- **Mensajes de Estado**: Feedback visual para operaciones CRUD

---

## 🔧 Funcionalidades Técnicas

### Sistema de Logging
- **Registro de Actividades**: Todas las operaciones CRUD se registran
- **Archivo de Log**: `clinic.log` con timestamps y detalles
- **Niveles de Log**: INFO, ERROR, DEBUG según corresponda

### Exportación de Datos
- **Formato CSV**: Exportación de propietarios y mascotas
- **Funcionalidad Reutilizable**: Utilidad genérica en `utils.py`
- **Headers Personalizables**: Configuración flexible de columnas

### Panel de Administración
- **Configuración Avanzada**: Filtros, búsquedas y ordenamiento
- **Interfaz Personalizada**: Campos específicos para cada modelo
- **Acceso Seguro**: Autenticación requerida

---

## 🧪 Validación

### Validación de Datos
- **Formularios Django**: Validación automática de campos
- **Modelos**: Restricciones de base de datos
- **Vistas**: Validación adicional de lógica de negocio

---

## 📊 Estado del Proyecto

### Funcionalidades Implementadas ✅
- [x] CRUD completo para los modelos
- [x] Panel de administración configurado
- [x] Sistema de logging operativo
- [x] Exportación de datos en CSV
- [x] Historia clínica consolidada
- [x] Interfaz responsive con Bootstrap
- [x] Validación de formularios
- [x] Manejo de errores


---

## 🐛 Solución de Problemas

### Errores Comunes

#### Error de Migraciones
```bash
# Si hay problemas con migraciones
python manage.py makemigrations --empty clinic
python manage.py migrate
```

#### Problemas de Entorno Virtual
```bash
# Recrear entorno virtual
rm -rf venv/
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

#### Base de Datos Corrupta
```bash
# Recrear base de datos
rm db.sqlite3
python manage.py makemigrations clinic
python manage.py migrate
python manage.py createsuperuser
```

---

## 📝 Licencia

**Proyecto Académico** - Clínica Veterinaria "Amigos Peludos"

- **Uso**: Educativo y de demostración
- **Modificación**: Permitida con fines educativos
- **Comercialización**: Requiere autorización expresa
- **Autor**: Jonathan Cardona Calderon, Sandra Liliana Zapata Gallón, Bootcamp Python SoftServe
