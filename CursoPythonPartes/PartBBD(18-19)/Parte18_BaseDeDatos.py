import sqlite3

miConexion = sqlite3.connect("primeraBase")
miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))") #asi creamos una tabla 
miCursor.execute("INSERT INTO PRODUCTOS VALUES('PELOTA',25,'DEPORTES')")#asi agregamos un solo producto """
#aora vamos agragar multiples productos , pero las intrucciones de arriba no pueden repetirse entonces las pones entre comillas 
#creamos una tupla

variosProductos = [
    ("RAQUETA",125,"DEPORTES"),
    ("CAMPERA",525,"ROPA Y CALZADO"),
    ("MAX STEEL",125,"JUGUETES")
]#teniendo la tupla simplemente queda agregar
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)#los "?" representan los valorespor eso solo tres
"""
#y ahora vamos a leer lo que contiene las tablas

miCursor.execute("SELECT * FROM PRODUCTOS")#hacemos la llamada a la base de datos
VariosProductos = miCursor.fetchall()#y luego con el fetchall almacenamos todo en un tupla para luego verla

for p in VariosProductos:
    print(p)#esto muestra todo
    print("El nombre del producto es: ",p[0])#esto solo muestra el nombre
    print(p[1])#esto solo el valor 
    print(p[2])#y esto solo la seccion
"""

miConexion.commit()
miConexion.close()