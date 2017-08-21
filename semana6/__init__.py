#haga un programa que lea las ventas mensuales de todos los vendedores de la compañia ABC, muestre las ventas totales, el vendedor que mas vendio y el que menos vendio
#Fianlmente si ABC paso la meta mensual de 1 millon.
import pickle
def imprimir_lista(x):
    print("\nMi lista de supermercado...")
    for a in x:
        print(str((int(x.index(a)+1))) + ". " + a)

def imprimir_diccionario(w):
    print("\nMi lista de supermercado...")

    for art,  in w.items() :

        print("Vendedor: " + str(art)  )


def imprimir_diccionario(a):


        print(f"vendedor{c}: "+nombre)
        print("ventas totales: "+str(total))

        if c >= 1000000:
            print("si se logro la meta")
        else:
            print("no se llego a la meta")


if __name__ == "__main__":
    print("\t\ttCompañia ABC")

    diccionario = {}
while True:

    print("1.ventas de los vendedores")
    print("2. ventas totales")
    print("3. Ver lista")
    print("4. Salir")
    try:

            opc = int(input("Opcion: "))
    except ValueError:
            opc = 0

    if opc == 1:
         print("Ingresar ventas de los vendedores...")
         for c in [1,2,3]:

          nombre = input(f"Vendedor {c}: ")
          artInsertar = int(input("Ventas totales : "))
          total



    elif opc== 2:
        print("\t\t\tVentastas totales de la empresa")
        resultado = imprimir_diccionario(diccionario)

    elif opc == 3:

         imprimir_diccionario(diccionario)
    elif opc == 4:
        break
    else:
        print("ERROR: :opcion no valida")

print("Hasta luego! ")





