from unittest import TestCase
from semana8 import matematica

class TestSumar(TestCase):
    def test_sumar(self):
        resultado = matematica.sumar(1, 2)
        self.assertEqual(resultado, 3)
