"""
Módulo de persistencia en SQLite para la Clínica Veterinaria "Amigos Peludos".
Funciones para crear tablas y realizar operaciones CRUD.
"""

import sqlite3
import logging
from datetime import datetime
from typing import List, Tuple

from models import Dueno, Mascota, Consulta

# Se Determina la ruta de la base de datos junto al script
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'clinica_veterinaria.db')

# Configuración de logging específico para database
logger = logging.getLogger('database')

# --------------------------------------------------
# Inicialización y creación de tablas
# --------------------------------------------------

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Crea las tablas si no existen."""
    sql_duenos = (
        """
        CREATE TABLE IF NOT EXISTS duenos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            direccion TEXT
        )
        """
    )
    sql_mascotas = (
        """
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especie TEXT,
            raza TEXT,
            edad INTEGER,
            id_dueno INTEGER NOT NULL,
            FOREIGN KEY(id_dueno) REFERENCES duenos(id)
        )
        """
    )
    sql_consultas = (
        """
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            motivo TEXT,
            diagnostico TEXT,
            id_mascota INTEGER NOT NULL,
            FOREIGN KEY(id_mascota) REFERENCES mascotas(id)
        )
        """
    )
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql_duenos)
        cur.execute(sql_mascotas)
        cur.execute(sql_consultas)
        conn.commit()
        logger.info("Tablas SQLite iniciadas o ya existentes.")
    except Exception as e:
        logger.error(f"Error creando tablas SQLite: {e}")
    finally:
        conn.close()

# --------------------------------------------------
# CRUD Dueños
# --------------------------------------------------

def agregar_dueno(dueno: Dueno) -> int:
    """Inserta un nuevo dueño y devuelve su id"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO duenos (nombre, telefono, direccion) VALUES (?, ?, ?)",
            (dueno.nombre, dueno.telefono, dueno.direccion)
        )
        conn.commit()
        dueno_id = cur.lastrowid
        logger.info(f"Dueño insertado con id {dueno_id}")
        return dueno_id
    except Exception as e:
        logger.error(f"Error insertando dueño: {e}")
        raise
    finally:
        conn.close()


def listar_duenos() -> List[Tuple[int, Dueno]]:
    """Devuelve lista de instancias Dueno desde la base de datos"""
    conn = get_connection()
    duenos: List[Tuple[int, Dueno]] = []
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, nombre, telefono, direccion FROM duenos")
        for row in cur.fetchall():
            dueno = Dueno(row['nombre'], row['telefono'], row['direccion'])
            duenos.append((row['id'], dueno))
        logger.info(f"Se cargaron {len(duenos)} dueños desde DB")
    except Exception as e:
        logger.error(f"Error listando dueños: {e}")
    finally:
        conn.close()
    return duenos


def actualizar_dueno(id_dueno: int, dueno: Dueno) -> None:
    """Actualiza los datos de un dueño existente"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE duenos SET nombre = ?, telefono = ?, direccion = ? WHERE id = ?",
            (dueno.nombre, dueno.telefono, dueno.direccion, id_dueno)
        )
        conn.commit()
        logger.info(f"Dueño {id_dueno} actualizado")
    except Exception as e:
        logger.error(f"Error actualizando dueño {id_dueno}: {e}")
        raise
    finally:
        conn.close()


def eliminar_dueno(id_dueno: int) -> None:
    """Elimina un dueño por su id"""
    conn = get_connection()
    try:
        conn.execute("DELETE FROM duenos WHERE id = ?", (id_dueno,))
        conn.commit()
        logger.info(f"Dueño {id_dueno} eliminado")
    except Exception as e:
        logger.error(f"Error eliminando dueño {id_dueno}: {e}")
        raise
    finally:
        conn.close()


# --------------------------------------------------
# CRUD Mascotas
# --------------------------------------------------

def agregar_mascota(mascota: Mascota, id_dueno: int) -> int:
    """Inserta una mascota asociada a un dueño y devuelve su id"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO mascotas (nombre, especie, raza, edad, id_dueno) VALUES (?, ?, ?, ?, ?)",
            (mascota.nombre, mascota.especie, mascota.raza, mascota.edad, id_dueno)
        )
        conn.commit()
        mascota_id = cur.lastrowid
        logger.info(f"Mascota insertada con id {mascota_id}")
        return mascota_id
    except Exception as e:
        logger.error(f"Error insertando mascota: {e}")
        raise
    finally:
        conn.close()


def listar_mascotas() -> List[Mascota]:
    """Devuelve lista de instancias Mascota con referencias a Dueno"""
    conn = get_connection()
    mascotas: List[Mascota] = []
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT m.nombre, m.especie, m.raza, m.edad, d.nombre, d.telefono, d.direccion "
            "FROM mascotas m JOIN duenos d ON m.id_dueno = d.id"
        )
        for row in cur.fetchall():
            dueno = Dueno(row[4], row[5], row[6])
            mascotas.append(Mascota(row[0], row[1], row[2], row[3], dueno))
        logger.info(f"Se cargaron {len(mascotas)} mascotas desde DB")
    except Exception as e:
        logger.error(f"Error listando mascotas: {e}")
    finally:
        conn.close()
    return mascotas


def actualizar_mascota(id_mascota: int, mascota: Mascota, id_dueno: int) -> None:
    """Actualiza los datos de una mascota existente"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE mascotas SET nombre = ?, especie = ?, raza = ?, edad = ?, id_dueno = ? WHERE id = ?",
            (mascota.nombre, mascota.especie, mascota.raza, mascota.edad, id_dueno, id_mascota)
        )
        conn.commit()
        logger.info(f"Mascota {id_mascota} actualizada")
    except Exception as e:
        logger.error(f"Error actualizando mascota {id_mascota}: {e}")
        raise
    finally:
        conn.close()


def eliminar_mascota(id_mascota: int) -> None:
    """Elimina una mascota por su id"""
    conn = get_connection()
    try:
        conn.execute("DELETE FROM mascotas WHERE id = ?", (id_mascota,))
        conn.commit()
        logger.info(f"Mascota {id_mascota} eliminada")
    except Exception as e:
        logger.error(f"Error eliminando mascota {id_mascota}: {e}")
        raise
    finally:
        conn.close()

# --------------------------------------------------
# CRUD Consultas
# --------------------------------------------------

def agregar_consulta(consulta: Consulta, id_mascota: int) -> int:
    """Inserta una consulta y devuelve su id."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO consultas (fecha, motivo, diagnostico, id_mascota) VALUES (?, ?, ?, ?)",
            (consulta.fecha.isoformat(), consulta.motivo, consulta.diagnostico, id_mascota)
        )
        conn.commit()
        consulta_id = cur.lastrowid
        logger.info(f"Consulta insertada con id {consulta_id}")
        return consulta_id
    except Exception as e:
        logger.error(f"Error insertando consulta: {e}")
        raise
    finally:
        conn.close()


def listar_consultas() -> List[Consulta]:
    """Devuelve lista de instancias Consulta con referencia a Mascota"""
    conn = get_connection()
    consultas: List[Consulta] = []
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT c.fecha, c.motivo, c.diagnostico, m.nombre, m.especie, m.raza, m.edad, d.nombre, d.telefono, d.direccion "
            "FROM consultas c "
            "JOIN mascotas m ON c.id_mascota = m.id "
            "JOIN duenos d ON m.id_dueno = d.id"
        )
        for row in cur.fetchall():
            dueno = Dueno(row[7], row[8], row[9])
            mascota = Mascota(row[3], row[4], row[5], row[6], dueno)
            fecha = datetime.fromisoformat(row[0])
            consultas.append(Consulta(fecha, row[1], row[2], mascota))
        logger.info(f"Se cargaron {len(consultas)} consultas desde DB")
    except Exception as e:
        logger.error(f"Error listando consultas: {e}")
    finally:
        conn.close()
    return consultas


def actualizar_consulta(id_consulta: int, consulta: Consulta, id_mascota: int) -> None:
    """Actualiza los datos de una consulta existente"""
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE consultas SET fecha = ?, motivo = ?, diagnostico = ?, id_mascota = ? WHERE id = ?",
            (consulta.fecha.isoformat(), consulta.motivo, consulta.diagnostico, id_mascota, id_consulta)
        )
        conn.commit()
        logger.info(f"Consulta {id_consulta} actualizada")
    except Exception as e:
        logger.error(f"Error actualizando consulta {id_consulta}: {e}")
        raise
    finally:
        conn.close()


def eliminar_consulta(id_consulta: int) -> None:
    """Elimina una consulta por su id"""
    conn = get_connection()
    try:
        conn.execute("DELETE FROM consultas WHERE id = ?", (id_consulta,))
        conn.commit()
        logger.info(f"Consulta {id_consulta} eliminada")
    except Exception as e:
        logger.error(f"Error eliminando consulta {id_consulta}: {e}")
        raise
    finally:
        conn.close()


# Inicializar la base de datos al importar el módulo
init_db()
