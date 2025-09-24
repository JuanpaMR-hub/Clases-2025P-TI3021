import os
os.system('cls')
# Asociación

class Usuario:
    #CONSTRUCTOR
    def __init__(self,username:str,password:str,email:str):
        self.username = username
        self.password = password
        self.email = email
        
    #METODOS
    def info(self):
        print("-------------------------")
        print("Username: ",self.username)
        print("Email: ",self.email)
        
    def autentificar(self,intento_username:str,intento_password:str):
        if intento_username == self.username:
            if intento_password == self.password:
                print("Ta bien, bienvenido!")
            else:
                print("Contraseña incorrecta!!!!")
        else:
            print("ERROR!!! Username incorrecto")
            
            
class Pago:
    def __init__(self,nombre_usuario,contraseña,email,monto_a_pagar:float, monto_pagado:float):
        self.usuario = Usuario(nombre_usuario,contraseña,email)
        self.monto_a_pagar = monto_a_pagar
        self.monto_pagado = monto_pagado
        self.diferencia = monto_a_pagar - monto_pagado
        
    
# u1 = Usuario("pedritoXX","pass123","PeDrItOxx@hotmail.com")

#Asociacion -> se asocian datos
#p1 = Pago(u1.username,100,100)
# print(p1.nombre_usuario)

#Agregacion -> Agrego un objeto dentro de otro
#p1 = Pago(u1,100,100)
#print(p1.usuario.username)

#Composición -> Se crea un objeto dentro de otro
p1 = Pago("pedritoXX","pass123","PeDrItOxx@hotmail.com",100,100)
print(p1.usuario.username)

# ------------- ACTIVIDAD ---------------------
# Crear una clase llamada arma
# Crear una clase personaje (que sea como un personaje de juego rpg)
# Añada un metodo llamado atacar que, dependiendo del ataque del arma, imprima la cantidad de daño que hace
# Crear un objeto de cada uno
# Agregar el arma en el objeto personaje
# Llamar al metodo atacar
