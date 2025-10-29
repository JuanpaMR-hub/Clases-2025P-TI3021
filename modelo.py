import oracledb

username = ""
password = ""
host = ""
port = 0
service_name = ""

class Persona:
    def __init__(self,nombre:str):
        self.nombre = nombre
        
    def info(self):
        info = f"------------------\nNombre: {self.nombre}"
        return info
    

# Este metodo es muy directo e ineficiente, por ello pueden crear una clase ConexiónBD que contenga metodos y solamente le pasamos las querys
# Dichas querys las creamos en este modelo
class GestionPersona:
    def guardar_persona(persona:Persona):
        try:
            with oracledb.connect(user = username,password = password, host = host, port = port, service_name = service_name) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO PERSONA VALUES (:nombre)",[persona.nombre])
                    conn.commit()
        except Exception as e:
            raise TypeError(e)
            
    # D.R.Y

            

        
    def mostrar_personas():
        try:
            with oracledb.connect(user = username,password = password, host = host, port = port, service_name = service_name) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM PERSONA")
                    return cursor.fetchall()
        except Exception as e:
            raise TypeError(e)