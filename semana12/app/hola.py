"""
Este es el modulo para chotiar
a la gente de la UIP
"""
class Hola(object):
    """
    Esta es la clase hola que permite chotiar
    """
    def __init__(self, nombre):
        """
        Este es el metodo constructor de la clase.
        Crea una instancia de: class: Hola
        :param nombre: nombre para el suludo
        :type nombre: str
        """
        self.nombre = nombre

    def saludar(self):
        """
        Este es el metodo para chotear a la gente.
        Usa el atributo nombre y lo imprime.
        """
        print("Hola, %s"% self.nombre)

    def getNombre(self):
        """"
        Este es el metodo para enviar el valor del nombre.
        :return: nombre usado en el saludo
        """
        return self.nombre