# Herencia
import os
os.system('cls')
class Personaje:
    def __init__(self,nombre:str,vida:int):
        self._nombre = nombre
        self.vida = vida
        
    def info(self):
        print("------------------------------------")
        print("Nombre: ",self._nombre)
        print("Vida: ",self.vida)
        
class Barbaro(Personaje):
    def __init__(self,nombre:str,vida:int):
        super().__init__(nombre,vida)
        
    def info(self):
        super().info()
        print("Clase: Barbaro")
        
#Clase mago se extiende de personaje
class Mago(Personaje):
    def __init__(self,nombre,vida, mana): # INIT DEL MAGO
        super().__init__(nombre,vida) # INIT DEL PERSONAJE
        self.mana = mana
        
    def info(self):
        super().info()
        print("Mana: ", self.mana)
        print("Clase: Mago")
        
#D.R.Y
# Don't Repeat Yourself
        
        
b1 = Barbaro("Dave",100)
m1 = Mago("Merlin",80,100)

b1.info()
m1.info()
        
        