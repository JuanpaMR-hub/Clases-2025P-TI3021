# En el modelo estarán solo las clases que vamos a utilizar

class Libro:
    def __init__(self,id_libro:int,titulo:str,autor:str):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        
        
class Cliente:
    def __init__(self,id_cliente:int,nombre:str,apellido:str):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        
    def __repr__(self):
        return self.nombre + " "+self.apellido
        

class Membresia:
    def __init__(self,id_membresia:int,nombre:str,beneficios:list[str]):
        self.id_membresia = id_membresia
        self.nombre = nombre
        self.beneficios = beneficios
        
class Prestamo:
    def __init__(self,id_prestamo:int,fecha_prestamo:str,fecha_devolucion:str):
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
   
# Biblioteca agrega libro y cliente, en una relación de uno a muchos, por ende se usa una lista para cada uno    
class Biblioteca:
    def __init__(self,id_libro:int,nombre:str):
        self.id_libro = id_libro
        self.nombre = nombre
        self.libros: list[Libro] = []
        self.clientes:list[Cliente] = []
        
    def agregar_cliente(self,cliente:Cliente):
        # Comprobamos que es un cliente
        if isinstance(cliente,Cliente):
            self.clientes.append(cliente)
            print("Cliente agregado! ")
        else:
            print("Ese no es un cliente")
        
    def agregar_libro(self,libro:Libro):
        if isinstance(libro,Libro):
            self.libros.append(libro)
        else:
            print("Ese no es un libro")
        
    def mostrar_clientes(self):
        print("----- Clientes ------")
        for cliente in self.clientes:
            print(cliente)
        print("---------------------")
            
    def buscar_cliente(self,id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
            
#------------------------------------------------------


# Instanciamos la biblioteca y un cliente
b1 = Biblioteca(1,"Biblio Nacional")
c1 = Cliente(1,"Pablo","Picasso")


b1.agregar_cliente(c1)

