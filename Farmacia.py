import json
from os import system
from datetime import date


boolGeneral = True
while boolGeneral == True:
    Eleccion = int(input("---Bienvenido a FarmCamp---\n1. Compras\n2. Ventas \n3. Salir\n\n A qué apartado deseas acceder?: "))

    if Eleccion == 1: 
        print("---COMPRAS---")

    elif Eleccion == 2:
        print("---VENTAS---")

    elif Eleccion == 3: 
        input("Gracias  por preferir FarmCamp, nos vemos luego :)")
        system("cls")
        boolGeneral = False
    
    else: 
        input("Esta no es una opción válida, presione ENTER para continuar")
        system("cls")