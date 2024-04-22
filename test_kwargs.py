from kwargs import buscar_datos
from kwargs import database
import unittest

class testkwargs (unittest.TestCase):
    def test_1(self):
        resultado = buscar_datos ("Santiago", 'Alberto', 'Ortega', 'Flores', **database) 
        self.assertEqual(resultado, {'persona2': {'primer_nombre': 'Santiago',"segundo_nombre": "Alberto","primer_apellido": "Ortega","segundo_apellido": "Flores"}})

    def test_2(self):
        resultado = buscar_datos ("Lionel", 'Andres', 'Messi', 'Cuccittini', **database) 
        self.assertEqual(resultado, {'persona1': {'primer_nombre': 'Lionel',"segundo_nombre": "Andres","primer_apellido": "Messi","segundo_apellido": "Cuccittini"}})

    def test_3(self):
        resultado = buscar_datos ("Lionel", 'Andres', **database)
        self.assertEqual(resultado, {})

    def test_4(self):
        resultado = buscar_datos ("Juan", 'Roman', 'Riquelme', 'Velazquez', **database) 
        self.assertEqual(resultado, {'persona3': {'primer_nombre': 'Juan',"segundo_nombre": "Roman","primer_apellido": "Riquelme", "segundo_apellido": "Velazquez"}})

    
unittest.main()

