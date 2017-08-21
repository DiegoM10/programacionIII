from app import persona

if __name__ == "__main__":
    print("Bienvenido")
    nombre = input("NOMBRE>")
    edad = int(input("EDAD>"))
    p1 = persona.persona(nombre, edad)
    print(p1.es_mayor_edad())