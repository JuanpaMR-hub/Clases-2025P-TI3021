from controlador import *
import os
os.system('cls')


menu = """
MENU
1. Crear Dueño
2. Ver Dueños
3. Crear Mascotas
4. Ver mascotas
0. Salir
"""

while True:
    print(menu)
    opcion = input("Ingrese opcion: ")
    if opcion == "1":
        crear_dueño()
    elif opcion == "2":
        ver_dueños()
    elif opcion == "3":
        crear_mascota()
    elif opcion=="4":
        ver_mascotas()
    elif opcion  == "0":
        print("Adios!")
        break
    else:
        print("Ese no es una opción valida")