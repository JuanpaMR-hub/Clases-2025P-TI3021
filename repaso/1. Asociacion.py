import os
os.system('cls')


class Personaje:
    # Constructor
    def __init__(self,nombre,vida):
        self.nombre = nombre
        self.vida = vida
        
    # Metodos
    def info(self):
        print("---------------")
        print("Nombre: ",self.nombre)
        print("Vida: ",self.vida)
        
    def atacar(self,arma):
        print(f"Has atacado con {arma.ataque} puntos de daño!")

        
class Arma:
    def __init__(self,nombre,ataque):
        self.nombre = nombre
        self.ataque = ataque
        
#---------------------------------------------------

# Para la asociación creamos dos objetos
arma1 = Arma("Gran Espada",100)
personaje1 = Personaje("Dave",1000)

# Ambos objetos interactuan entre ellos por medio de sus atributos

personaje1.atacar(arma1)
#Aqui personaje está interactuando con arma
