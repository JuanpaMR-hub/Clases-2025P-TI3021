class Mascota:
    __mascotas = []
    def __init__(self,nombre:str,especie:str, dueño:'Dueño'):
        self.nombre = nombre
        self.especie = especie
        self.dueño = dueño
        
    def guardar_mascota(self):
        Mascota.__mascotas.append(self)
        
    @staticmethod
    def mostrar_mascotas():
        return Mascota.__mascotas
    
    
class Dueño:
    __dueños = []
    def __init__(self,nombre:str,apellido:str):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas:list[Mascota] =[]
        
    def guardar_dueño(self):
        Dueño.__dueños.append(self)
        
    def agregar_mascota(self,mascota:Mascota):
        self.mascotas.append(mascota)
    def ver_mascotas(self):
        return self.mascotas
        
    @staticmethod
    def mostrar_dueños():
        return Dueño.__dueños
    
    @staticmethod
    def buscar_dueño_por_nombre(nombre:str):
        for dueño in Dueño.__dueños:
            if dueño.nombre == nombre:
                return dueño
        return None