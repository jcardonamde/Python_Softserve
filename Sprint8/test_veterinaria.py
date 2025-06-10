import os
import unittest
from datetime import datetime
from unittest.mock import patch


# Importar desde los módulos del proyecto
from models import Dueno, Mascota, Consulta
from storage import (
    CSV_MASCOTAS,
    JSON_CONSULTAS,
    guardar_mascotas_csv,
    cargar_mascotas_csv,
    guardar_consultas_json,
    cargar_consultas_json
)
from utils import input_int


class TestModels(unittest.TestCase):
    def test_dueno_str(self):
        dueno = Dueno('Juan Perez', '3001234567', 'Calle 123')
        expected = "Dueño: Juan Perez | Tel: 3001234567 | Dir: Calle 123"
        self.assertEqual(str(dueno), expected)

    def test_mascota_str(self):
        dueno = Dueno('Ana Maria', '3127654321', 'Avenida 45')
        mascota = Mascota('Luna', 'Perro', 'Labrador', 3, dueno)
        # str incluirá varias líneas, comprobamos que contenga la información clave
        res = str(mascota)
        self.assertIn("Mascota: Luna", res)
        self.assertIn("Especie: Perro", res)
        self.assertIn("Raza: Labrador", res)
        self.assertIn("Edad: 3 años", res)
        self.assertIn("Dueño: Ana Maria", res)

    def test_consulta_str(self):
        dueno = Dueno('Carlos Ruiz', '3100001111', 'Calle Falsa 789')
        mascota = Mascota('Milo', 'Gato', 'Siames', 2, dueno)
        fecha = datetime(2022, 5, 10, 14, 30)
        consulta = Consulta(fecha, 'Chequeo general', 'Saludable', mascota)
        res = str(consulta)
        self.assertIn("[2022-05-10 14:30] Consulta de 'Milo'", res)
        self.assertIn("Motivo: Chequeo general", res)
        self.assertIn("Diagnóstico: Saludable", res)

class TestSerialization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Asegurar que no existan archivos antiguos antes de pruebas
        if os.path.exists(CSV_MASCOTAS):
            os.remove(CSV_MASCOTAS)
        if os.path.exists(JSON_CONSULTAS):
            os.remove(JSON_CONSULTAS)

    @classmethod
    def tearDownClass(cls):
        # Limpiar archivos generados tras pruebas
        if os.path.exists(CSV_MASCOTAS):
            os.remove(CSV_MASCOTAS)
        if os.path.exists(JSON_CONSULTAS):
            os.remove(JSON_CONSULTAS)

    def test_guardar_y_cargar_mascotas_csv(self):
        # Crear objeto Mascota y usar guardar
        dueno = Dueno('Luisa Torres', '3209876543', 'Carrera 7')
        mascota = Mascota('Rocky', 'Perro', 'Bulldog', 4, dueno)
        mascotas_list = [mascota]

        guardar_mascotas_csv(mascotas_list)
        self.assertTrue(os.path.exists(CSV_MASCOTAS))

        # Cargar desde archivo y comparar
        cargadas = cargar_mascotas_csv()
        self.assertEqual(len(cargadas), 1)
        m2 = cargadas[0]
        self.assertEqual(m2.nombre, 'Rocky')
        self.assertEqual(m2.especie, 'Perro')
        self.assertEqual(m2.raza, 'Bulldog')
        self.assertEqual(m2.edad, 4)
        self.assertEqual(m2.dueno.nombre, 'Luisa Torres')
        self.assertEqual(m2.dueno.telefono, '3209876543')
        self.assertEqual(m2.dueno.direccion, 'Carrera 7')

    def test_guardar_y_cargar_consultas_json(self):
        # Para consultas, necesitamos una Mascota cargada primero
        dueno = Dueno('Mario Lopez', '3154443333', 'Diagonal 10')
        mascota = Mascota('Bella', 'Gato', 'Persa', 5, dueno)
        mascotas_list = [mascota]

        fecha = datetime(2021, 12, 1, 9, 0)
        consulta = Consulta(fecha, 'Vacunación', 'Rabia aplicada', mascota)
        consultas_list = [consulta]

        # Guardar ambas estructuras
        guardar_mascotas_csv(mascotas_list)
        guardar_consultas_json(consultas_list)

        self.assertTrue(os.path.exists(JSON_CONSULTAS))

        # Recargar mascotas y luego consultas
        cargadas_mascotas = cargar_mascotas_csv()
        cargadas_consultas = cargar_consultas_json(cargadas_mascotas)

        self.assertEqual(len(cargadas_consultas), 1)
        c2 = cargadas_consultas[0]
        self.assertEqual(c2.motivo, 'Vacunación')
        self.assertEqual(c2.diagnostico, 'Rabia aplicada')
        self.assertEqual(c2.mascota.nombre, 'Bella')
        self.assertEqual(c2.fecha, fecha)

    def test_cargar_sin_archivos_devuelve_listas_vacias(self):
        # Asegurarnos de que no existan archivos
        if os.path.exists(CSV_MASCOTAS):
            os.remove(CSV_MASCOTAS)
        if os.path.exists(JSON_CONSULTAS):
            os.remove(JSON_CONSULTAS)

        vacio_mascotas = cargar_mascotas_csv()
        vacio_consultas = cargar_consultas_json([])
        self.assertEqual(vacio_mascotas, [])
        self.assertEqual(vacio_consultas, [])

class TestInputValidation(unittest.TestCase):
    def test_input_int_valido(self):
        # Simular input usando patch de unittest.mock
        from unittest.mock import patch
        with patch('builtins.input', return_value='5'):
            val = input_int('Ingresa un número: ', min_val=1, max_val=10)
            self.assertEqual(val, 5)

    def test_input_int_fuera_de_rango_y_reintento(self):
        from unittest.mock import patch
        inputs = ['-1', 'abc', '11', '7']  # varios intentos hasta un valor válido
        with patch('builtins.input', side_effect=inputs):
            val = input_int('Ingresa un número: ', min_val=0, max_val=10)
            self.assertEqual(val, 7)

if __name__ == '__main__':
    unittest.main(verbosity=2)
