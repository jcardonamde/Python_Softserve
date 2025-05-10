# 📬 Validador y Gestor de Correos Electrónicos - Biblioteca UTV

Aplicación de consola desarrollada en Python que permite registrar, validar, clasificar y administrar correos electrónicos de estudiantes y docentes de la Universidad Tecnológica del Valle.

---

## 📌 Características

- Menú interactivo para realizar operaciones básicas.
- Validación de correos electrónicos mediante expresiones regulares.
- Clasificación automática entre correos de **estudiantes** y **docentes**.
- Almacenamiento en memoria con estructura de diccionario.
- Búsqueda por coincidencias parciales o totales.
- Interfaz simple, clara y robusta.

---

## 🎯 Requisitos Funcionales

1. Registrar correos electrónicos válidos.
2. Validar formato y dominio institucional.
3. Mostrar lista completa de correos registrados.
4. Buscar correos específicos desde consola.
5. Salir del programa sin errores.

---

## 🛠️ Tecnologías y conceptos usados

- Python 3
- Expresiones regulares (`re`)
- Tipos de datos primitivos (`str`, `list`, `dict`)
- Ciclos (`while`, `for`)
- Condicionales (`if`, `elif`, `else`)
- Manejo de strings y búsqueda parcial

---

## 🚀 Instrucciones de uso

1. Asegúrate de tener Python 3 instalado.
2. Descarga o clona este repositorio.
3. Ejecuta el script desde consola:

```bash
python gestor_correos.py

4. Sigue las instrucciones en pantalla para registrar, ver o buscar correos.

<br>

## 🧪 Ejemplos de correos válidos
| Correo electrónico                  | Clasificación |
| ----------------------------------- | ------------- |
| `juan.perez@estudiante.utv.edu.co`  | Estudiante    |
| `maria.garcia@utv.edu.co`           | Docente       |
| `luis_mendez@estudiante.utv.edu.co` | Estudiante    |
| `doc.castro@utv.edu.co`             | Docente       |

## 📁 Estructura del código
gestor_correos/
├── gestor_correos.py   # Archivo principal con la lógica de la aplicación
└── README.md           # Documentación del proyecto

## 📄 Licencia
Este proyecto ha sido desarrollado con fines académicos para el Bootcamp de Python Softserve. 
Puedes usar, modificar y distribuir libremente este código para fines educativos o personales.
No se permite su uso con fines comerciales sin autorización.