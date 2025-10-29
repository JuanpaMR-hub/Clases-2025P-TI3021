# 0. Instalar libreria oracledb
# 1. Importar libreria ✅
# 2. Crear la conexión ✅
# 3. Crear un cursor ✅
# 4. Con el cursor ejecutar la query ✅

import oracledb

# CREDENCIALES
#Las credenciales se obtienen de la misma base de datos
# Debe modificarlas para la base de datos suya
username = ""
password = ""
host = ""
port = 0
service_name = ""

with oracledb.connect(user = username,password = password, host = host, port = port, service_name = service_name) as conn:
    print("Conexion realizada exitosamente!")
    with conn.cursor() as cursor:
        # EJECUTAR NUESTRAS QUERYS
        
        # CREATE
        # query = "CREATE TABLE PERSONA(nombre varchar(50))"
        # cursor.execute(query)
        
        # INSERT - utilizando bind variables
        # cursor.execute("INSERT INTO PERSONA VALUES (:nombre)",['Pablo Picasso'])
        # conn.commit()
        
        
        #SELECT
        # cursor.execute("SELECT * FROM HELP")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        
        
        # SELECT WHERE
        cursor.execute("SELECT * FROM HELP WHERE SEQ = :seq",[4])
        rows = cursor.fetchall()
        for row in rows:
            print(row)