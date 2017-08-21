from unittest import TestCase
from app import persona


class TestPersona(TestCase):
    def setUp(self):
        self.persona = persona.Persona("petra", 50)

    def test_es_mayor_edad(self):
        self.assertEqual(self.persona.es_mayor_edad(), "MAYOR")
