from urllib.request import urlopen
import json
import os 
os.system('cls')

url = "https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Ingrese pokemon: ")

try: 
    with urlopen(url+pokemon) as respuesta:
        data_bytes = respuesta.read()     
except Exception as e:
    print("Pokemon no encontrado :(")
else:
        data = json.loads(data_bytes)
        id = data.get('id')
        nombre = data.get('name')
        orden = data.get('order')
        
        print("---- POKEMON ENCONTRADO -----")
        print(f"Id: {id}\n"+
              f"Nombre: {nombre}\n"+
              f"Orden: {orden}")
        for tipo in data.get('types'):
            print(f"- {tipo.get('type').get('name')}")