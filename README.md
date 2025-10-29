# Clase 12 - Conexión a Bases de Datos


### ¿Que vimos en la clase?
En esta clase vimos como podemos realizar la conexión desde python a una base de datos a elección, en esta ocasión utilizamos oracle


### ¿Como conectar a la BD?
Para poder realizar la conexión se necesita realizar los siguientes pasos

0. Instalar libreria oracledb
1. Importar libreria 
2. Crear la conexión 
3. Crear un cursor 
4. Con el cursor ejecutar la query 

### ¿Como se puede involucrar en nuestra arquitectura MVC?

En nuestra clase para gestionar las entidades, en su metodo de "guardar" se debe de hacer la conexión para ejecutar dicha query

En el ejemplo se hace de manera directa, pero esto se les pedirá lo siguiente:
1. Crear una clase ConexionBD
2. En dicha clase existirán los metodos para hacer las operaciones necesarias
3. Los metodos solamente esperarán datos que les indicarán a que tabla realizar y que datos insertar o traer
4. En los metodos de las clases Gestion, deberá ser para la creación de la query