###############################################
import os
from modelo import *
from controlador import *
os.system('cls')
###############################################

# En la vista se muestra solo lo visual, es decir nuestro menú

def menu():
    print("## MENU ####")
    print("1. Ver Clientes")
    print("2. Agregar Cliente")
    print("3. Ver Libros")
    print("4. Agregar Libros")
    print("0. Salir")
    try:
        opcion = int(input("Elija una opción: "))
    except ValueError as e:
        print("Porfavor ingrese un numero")
    else:
        return opcion
    

# Solo mostraremos el menu
if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == 1:
            b1.mostrar_clientes()
        elif opcion == 2:
            # Aqui creamos el cliente en el controlador para verificar todas sus credenciales
            cliente = crear_y_verificar_cliente()
            if cliente:
                b1.agregar_cliente(cliente)
        elif opcion == 0:
            print("Adios!")
            break
        else:
            print("Esa no es una opción valida")
        
