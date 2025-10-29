import os
os.system('cls')

# ------------- ACTIVIDAD ---------------------
# 1. Crear una clase llamada Usuario que contenga username, password y email como atributo
# 2. Dentro de Usuario crear un metodo llamado autenticar que revise si el intento de ingresar del usuario coinicde con los datos del usuario guardado
# 3. Crear un usuario con credenciales
# 4. Pedir credenciales al usuario por consola
# 5. Usando el metodo autenticar verifique si los datos ingresados son los correctos


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
        
    def autentificar(self,intento_password:str):
            return self.password == intento_password
        

u1 = Usuario("pedritoXX","pass123","PeDrItOxx@hotmail.com")
u2 = Usuario("miauLover","cat123cat","correo_profesional@dominio.com")

lista_usuarios = [u1,u2]


intento_username = input("Ingrese su username: ")
intento_password = input("Ingrese su contraseña: ")

usuario_encontrado = None
for usuario in lista_usuarios:
    if usuario.username == intento_username:
        usuario_encontrado = usuario

if usuario_encontrado:
    if usuario_encontrado.autentificar(intento_password):
        print("Bienvenido al sistema! ✔")
    else:
        print("Error, contraseña incorrecta ❌")
else:
    print(f"Usuario con username {intento_username} no encontrado")
