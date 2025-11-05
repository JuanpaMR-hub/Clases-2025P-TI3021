#pip install requests
import requests
import os
os.system('cls')

url = "https://rickandmortyapi.com/api/episode/"

try:
    data = requests.get(url).json()
except Exception as e:
    print(e)
else:
    episodios = data.get('results')
    for episodio in episodios:
        print("-------------------------")
        print(episodio.get('name'))
        print(episodio.get('air_date'))
        print("Personajes: ")
        for personaje in episodio.get('characters'):
            try:
                nombre = requests.get(personaje).json().get('name')
            except Exception as e:
                print(e)
            else:
                print(f"- {nombre}")



