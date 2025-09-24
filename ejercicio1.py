import os
os.system('cls')

# Crear una clase Usuario -> username, password

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
        

u1 = Usuario("pedritoXX","pass123","PeDrItOxx@hotmail.com")
u2 = Usuario("miauLover","cat123cat","correo_profesional@dominio.com")


intento_username = input("Ingrese su username: ")
intento_password = input("Ingrese su contraseña: ")
u1.autentificar(intento_username,intento_password)

