from modelo import *


def crear_persona(nombre:str):
    if nombre:
        p = Persona(nombre)
        try:
            GestionPersona.guardar_persona(p)
        except Exception as e:
            raise TypeError(e)
    else:
        raise TypeError("Nombre no puede ser vacio")
    
    
def mostrar_personas() -> list[Persona]:
    """ 
    Trae los registros del modelo GestionPersona como lista de tuplas 
    y las convierte en el objeto persona.
    Luego de convertirlas las guarda en una lista de objetos
    Returns:
        list[Persona]: Un listado de objetos persona
    """
    
    personas = []
    for registro in GestionPersona.mostrar_personas():
        nombre = registro[0]
        p = Persona(nombre)
        personas.append(p)
    return personas
        