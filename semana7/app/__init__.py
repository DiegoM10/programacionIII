from model.participantes import Participante
import re
if __name__ == "__main__":
    listaParticipantes = []
    while (True):
        print("ASISTENCIA EVENTO")
        print("1. Ingresar participante")
        print("2. Ver estadisticas")
        print("3. ver todos los participantes")
        print("4. Salir")
        try:
            opc = int(input("OPCION> "))
        except:
            opc = 0
        if opc == 1:
             print("\nINGRESAR PARTICIPANTE")
             while (True):
                 nombre = input("Nombre y apellido: ")
                 if re.search("^[A-Z][a-z]*(\s[A-Z][a-z]*)?$", nombre):
                     break
                 else:
                     print("ERROR :: Nombre no valido")
             while (True):
                try:
                   edad = int(input("Edad: "))
                except:
                  edad = 0
                if edad>0:
                   break
                else:
                  print("ERROR :: Edad No Valido")
             while (True):
               sexo = input("Sexo(M/F): ").upper()
               if sexo.upper() == "M" or sexo.upper() == "F":
                     break
               else:
                     print("ERROR :: SEXO NO VALIDO")

             participante = Participante(nombre,edad,sexo)

             listaParticipantes.append(participante)
        elif opc == 2:
            masculino = 0
            femenino = 0
            mayoredad = 0
            print("\nVER ESTADISTICAS")
            print("Total de participantes: "+str(len(listaParticipantes)))
            for p in listaParticipantes:
                if p.get_sexo() == "M":
                    masculino += 1
                else:
                    femenino += 1
                if p.get_edad() >= 18:
                    mayoredad += 1
            print("Total de Hombres: "+str(masculino))
            print("Total de Mujeres: "+str(femenino))
            print("Total de mayores de edad: "+str(mayoredad))
        elif opc ==3:
            print("\nVER TODOS")
            for p in listaParticipantes:
                p.mostrar()
        elif opc == 4:
            break
        else:
            print("ERROR")