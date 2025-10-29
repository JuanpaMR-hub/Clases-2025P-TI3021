#Objetos en python

# Clase persona  -> nombre, apellido, juego_favorito
import os
os.system('cls')

class Persona:
    #Constructor -> instancia el objeto
    def __init__(self,nombre:str,apellido:str,juego_favorito:str="Ninguno"):
        # Atributos del objeto
        self.nombre = nombre
        self.apellido = apellido
        self.juego_favorito = juego_favorito
    
    def info(self):
        # con self se refiere al objeto
        print("----------------------------------------")       
        print("Nombre: ",self.nombre)       
        print("Apellido: ",self.apellido)
        print("Juego Favorito: ",self.juego_favorito)
        

#-------------- FUERA DE LA CLASE ---------------------
# Crear 4 personas y guardarlas dentro de una lista
persona1 = Persona("Pablo","Picasso","Pinturillo")
persona2 = Persona("Diego","Nepomuceno")
persona3 = Persona("Jose","De los Remedios")
persona4 = Persona("Francisco","Ciprianos")

lista_personas = [persona1, persona2,persona3,persona4]

for persona in lista_personas:
    persona.info()
    
    