import os
os.system('cls')

#Agregación 1 a muchos
# Como ahora son muchas armas, no podemos pasarle en los parametros Arma, porque ¿que pasaria si son dos armas? ¿y si son tres? 
# Mejor haremos una lista y con un metodo las iremos agregando

class Arma:
    def __init__(self,nombre,ataque):
        self.nombre = nombre
        self.ataque = ataque
        
    #Metodo para que al momento de ser visualizada se represente con su nombre
    def __repr__(self):
        return self.nombre


class Personaje:
    # Constructor
    def __init__(self,nombre:str,vida:int):
        self.nombre = nombre
        self.vida = vida
        self.armas = []
        
    # Metodos
    def info(self):
        print("---------------")
        print("Nombre: ",self.nombre)
        print("Vida: ",self.vida)
        
    def agregar_arma(self,arma_a_agregar:Arma):
        #Verificamos si el arma es de clase Arma
        if isinstance(arma_a_agregar,Arma):
            self.armas.append(arma_a_agregar)
        else:
            print("Esa no es un arma")



        
#---------------------------------------------------

# Aqui crearemos dos objetos arma
arma1 = Arma("Gran Espada",100)
arma2 = Arma("Daga",50)

# y un objeto personaje
personaje1 = Personaje("Dave",1000)

# Ahora usando el metodo de personaje, agregaremos ambas armas

personaje1.agregar_arma(arma1)
personaje1.agregar_arma(arma2)

print("Armas del personaje: ",personaje1.armas)

