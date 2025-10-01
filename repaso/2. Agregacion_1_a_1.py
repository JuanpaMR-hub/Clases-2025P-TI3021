import os
os.system('cls')

#Agregación 1 a 1
# Le pasaremos el objeto agregado en los mismos parametros
#¿Que pasaria si no le pasamos arma? ¿Es necesario que tenga una?
# def __init__(self,nombre,vida, arma = None)


class Arma:
    def __init__(self,nombre,ataque):
        self.nombre = nombre
        self.ataque = ataque


class Personaje:
    # Constructor
    def __init__(self,nombre:str,vida:int,arma:Arma = None):
        self.nombre = nombre
        self.vida = vida
        self.arma = arma
        
    # Metodos
    def info(self):
        print("---------------")
        print("Nombre: ",self.nombre)
        print("Vida: ",self.vida)
        
    def atacar(self):
        #Con este cambio podemos acceder al arma desde el mismo objeto
        if self.arma:
            print(f"Has atacado con {self.arma.ataque} puntos de daño")
    



        
#---------------------------------------------------

# Para la agregación se puede definir que un objeto es agregado en otro

#Podemos definir un valor por defecto
#Aqui crearemos dos objetos 
arma1 = Arma("Gran Espada",100)

#Se le agrega el objeto arma creado a personaje
personaje1 = Personaje("Dave",1000,arma1)

