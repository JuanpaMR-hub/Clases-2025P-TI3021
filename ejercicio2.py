import os
os.system('cls')
# ------------- ACTIVIDAD ---------------------
# 1. Crear una clase llamada arma
# 2. Crear una clase personaje (que sea como un personaje de juego rpg)
# 3. Añada un metodo llamado atacar que, dependiendo del ataque del arma, imprima la cantidad de daño que hace
# 4. Crear un objeto de cada uno
# 5. Agregar el arma en el objeto personaje
# 6. Llamar al metodo atacar

class Arma:
    def __init__(self,nombre:str,danio:float,tipo:str):
        self.nombre = nombre
        self.danio = danio
        self.tipo = tipo
        

class Personaje:
    def __init__(self,nombre:str,clase:str,arma:Arma):
        self.nombre = nombre
        self.clase = clase
        self.arma = arma
        
    def atacar(self):
        danio = self.arma.danio
        print(f"Has hecho {danio} puntos de daño!!")
    
    
arma = Arma("Espada curva",24,"Corte")
personaje = Personaje("Dave","Barbaro",arma)

personaje.atacar()