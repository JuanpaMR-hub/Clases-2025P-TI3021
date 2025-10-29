import os
from controlador import *
os.system('cls')
##############################

menu = """
MENU
1. Crear persona
2. Mostrar personas
0. Salir
"""

while True:
    print(menu)
    opcion = input("Ingrese opción: ")
    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        try:
            crear_persona(nombre)
        except Exception as e:
            print(e)
        else:
            print("Persona creada exitosamente")
    elif opcion == "2":
        for persona in mostrar_personas():
            print(persona.info())
    elif opcion == "0":
        print("Adios!")
        break
    else:
        print("No es una opcion valida")