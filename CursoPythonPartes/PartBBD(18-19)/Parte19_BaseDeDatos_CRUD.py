import sqlite3 
"""miConexion = sqlite3.connect("Prueba_GraficaBBDD")
cursor = miConexion.cursor()
#creamos tabla"""

Conexion = sqlite3.connect("Prueba_GraficaBBDD")
cursor = Conexion.cursor()
#messagebox.showinfo("Estado de la coneccion","Se conecto corectamente con la base de datos")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Persona(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
DNI VARCHAR(10),
NOMBRE VARCHAR(50),
APELLIDO VARCHAR(50),
ANIO_DE_NACIMIENTO VARCHAR(11),
GMAIL VARCHAR(20))
''')

dni = "54122410"
nombre = "Elias"
apellido = "Pascual"
fecha = "26/08/2000"
gmail = "EliaspijaGorda@gmail.com"

cursor.execute("INSERT INTO Persona VALUES(NULL,'"+ dni + "','" + nombre + "','" + apellido + "','" + fecha + "','" + gmail + "')")
print("hola")
"""
#------------------- CREATED -------------
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_PRODUCTO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')


#creamos varios productos
VariosProductos = [
    ("RAQUETA",125,"DEPORTES"),
    ("CAMPERA",525,"ROPA Y CALZADO"),
    ("MAX STEEL",125,"JUGUETES"),
    ("HOT WHEELS",105,"JUGUETES")
]
#y los agregagamos
cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",VariosProductos)





#y tambien podemos agregar de a uno con un codigo diferente
cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'MAX STEEL','300','DEPORTES')")

#-----------------------READ-----------

cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION ='JUGUETES'")
productos = cursor.fetchall()
print(productos)

#----------------UPDATE---------------  
cursor.execute("UPDATE PRODUCTOS SET PRECIO = 130 WHERE NOMBRE_PRODUCTO = 'RAQUETA'")

#---------------DELATE--------------

cursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")"""



Conexion.commit()
Conexion.close()