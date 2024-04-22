from Factorial import factorial
import unittest

class testfactorial (unittest.TestCase):
    
    def test_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado,1)

    def test_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)

    def test_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)

    def test_4(self):
        resultado = factorial(4)
        self.assertEqual(resultado,24)

    def test_5(self):
        resultado = factorial(5)
        self.assertEqual(resultado, 120)

    def test_6(self):
        resultado = factorial(6)
        self.assertEqual(resultado, 720)

unittest.main()