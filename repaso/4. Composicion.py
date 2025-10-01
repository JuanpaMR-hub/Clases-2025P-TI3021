import os
os.system('cls')

# Composición
# Si el objeto contenedor es eliminado, los objetos que estan contenidos tambien se eliminan
# Para este caso lo que tenemos que hacer es crear un objeto dentro del objeto contenedor

        
class Arma:
    def __init__(self,nombre,ataque):
        self.nombre = nombre
        self.ataque = ataque
        
        
        
class Personaje:
    # Constructor
    def __init__(self,nombre,vida,nombre_arma,ataque):
        self.__nombre = nombre
        self.vida = vida
        #Creamos y guardamos un objeto de clase Arma
        self.arma = Arma(nombre_arma,ataque)
        
    # Metodos
    def info(self):
        print("---------------")
        print("Nombre: ",self.nombre)
        print("Vida: ",self.vida)
    
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
          
    def atacar(self):
        if self.arma:
            print("Has atacado con ",self.arma.ataque," puntos de daño")
        else:
            print("No tienes arma!")
        
        
        
#---------------------------------------------------

#Para este caso en la composición debemos pasarle todos los datos a personajes

p1 = Personaje("Dave",1000,"Gran Espada",100)
p1.atacar()