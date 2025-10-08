from modelo import *



def crear_dueño():
    nombre = input("Ingrese el nombre: ")
    if nombre:
        apellido = input("Ingrese apellido: ")
        if apellido:
            print("Nombre: ",nombre)
            print("Apellido: ",apellido)
            verificacion = input("Están los datos correctos? (y/n) ")
            if verificacion.lower() == "y":
                dueño = Dueño(nombre,apellido)
                dueño.guardar_dueño()
                print("Dueño creado exitosamente!")
            else:
                print("operacion cancelada")
        else:
            print("No se puede dejar un apellido vacio")
            
    else:
        print("No se puede dejar un nombre vacio")
        
        
def ver_dueños():
    for d in Dueño.mostrar_dueños():
        print("-----------------")
        print("Nombre: ",d.nombre)
        print("Apellido: ",d.apellido)
        
        
        
def crear_mascota():
    nombre = input("Ingrese el nombre: ")
    if nombre:
        especie = input("Ingrese la especie: ")
        if especie:
            dueño = input("Ingrese el nombre del dueño: ")
            dueño:Dueño = Dueño.buscar_dueño_por_nombre(dueño)
            if dueño:
                print("Nombre: ",nombre)
                print("Especie: ",especie)
                print("Dueño: ",dueño.nombre)
                verificacion = input("Están los datos correctos? (y/n) ")
                if verificacion.lower() == "y":
                    mascota = Mascota(nombre,especie,dueño)
                    mascota.guardar_mascota()
                    dueño.agregar_mascota(mascota)
                    print("Mascota creado exitosamente!")
                else:
                    print("operacion cancelada")
            else:
                print("Dueño no encontrado. Operacion cancelada")
        else:
            print("No se puede dejar un apellido vacio")
            
    else:
        print("No se puede dejar un nombre vacio")
        
        
def ver_mascotas():
    for m in Mascota.mostrar_mascotas():
        print("---------------")
        print("Nombre: ",m.nombre)
        print("Especie: ",m.especie)
        print("Dueño: ",m.dueño.nombre)