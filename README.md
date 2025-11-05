# Clase 13 - Consumo de APIs

## ¿Que vimos en esta clase?

Primeramente vimos que son las Application Programming Interfaces (API) con el famoso ejemplo del mesero
Para la parte práctica de esto, vimos dos APIs publicas para poder obtener los datos
- PokeApi
- RicknMortyAPI


## ¿Como hacer una consulta a la API?

### Manera 1 - urllib
La primera manera que usamos fue con la libreria que ya viene instalada con python **urllib**. Con esta libreria necesitamos guardar nuestros datos en un **json** para poder hacer uso de estos datos. Por ello importamos dicha libreria (json) en nuestro codigo

A modo de práctica hicimos una consulta a la api de PokeAPI para obtener información de diferentes pokemones

### Manera 2 - requests

Esta libreria, a diferencia de la anterior, es externa. Por lo cual tenemos que instalarla con pip `pip install requests`
Una vez instalada, la importamos y podemos hacer uso de esta

Es mas sencilla de utilizar que la anterior, pero de igual manera se tiene que pasar a json
