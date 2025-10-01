# El controlador se encargará de toda la logica que se encuentra fuera de la clase

from modelo import Cliente, b1

def crear_y_verificar_cliente() -> Cliente:
    cliente = None
    try:
        id = int(input("Ingrese el id del cliente: "))
        if b1.buscar_cliente(id):
            raise NameError("El cliente ya existe")
    except ValueError as e:
        print("El id tiene que ser un numero")
        
    except NameError as e:
        print(e)
        
    else:
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        cliente = Cliente(id,nombre,apellido)
    finally:
        return cliente