import os
os.system('cls')


class Personaje:
    # Constructor
    def __init__(self,nombre:str,vida:int):
        self.nombre = nombre
        self.vida = vida
        
    # Metodos
    def info(self):
        print("---------------")
        print("Nombre: ",self.nombre)
        print("Vida: ",self.vida)
    

        
        
# Herencia
# La clase Mago se deriva de Personaje
class Mago(Personaje):
    # Le agregamos los mismos parametros que necesita Personaje añadiendo los propios de Mago
    def __init__(self,nombre,vida,mana):
        #super() significa que vamos a llamar a lo que esté en la super clase, en este caso es Personaje
        super().__init__(nombre,vida) #- > Creamos un objeto Personaje
        self.mana = mana

#---------------------------------------------------


mago = Mago("Gandalf",100,100)
#Podemos acceder a los metodos de Personaje desde Mago
mago.info()

