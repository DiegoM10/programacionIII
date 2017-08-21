from unittest import TestCase
from semana8 import matematica

class TestRestar(TestCase):
    def test_restar(self):
        resultado = matematica.sumar(2, 1)
        self.assertEqual(resultado, 1)
