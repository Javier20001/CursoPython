from ast import Str
from tkinter import messagebox
import sqlite3

def conectar():
    Conexion = sqlite3.connect("Prueba_Grafica_BBDD")
    cursor = Conexion.cursor()
    messagebox.showinfo("Estado de la coneccion","Se conecto corectamente con la base de datos")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Persona(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DNI VARCHAR(10),
    NOMBRE VARCHAR(50),
    APELLIDO VARCHAR(50),
    AÑO_DE_NACIMIENTO VARCHAR(11),
    GMAIL VARCHAR(20),
    VISUAL NUMBER(1))
    ''')


def CrearPersona(nombre , apellido , Gmail, Fecha , DNi):
    Personas = [
    (DNi,nombre,apellido,Fecha,Gmail)
    ]
    Conexion = sqlite3.connect("Prueba_Grafica_BBDD")
    cursor = Conexion.cursor()
    cursor.executemany("INSERT INTO Persona VALUES(NULL,?,?,?,?,?,1)",Personas)
    messagebox.showinfo("Creacion","Se agrego correctamente")
    Conexion.commit()

def EliminarPersona(id ):
    Conexion = sqlite3.connect("Prueba_Grafica_BBDD")
    cursor = Conexion.cursor()
    cursor.execute("SELECT * FROM Persona WHERE ID == '"+ str(id) +"'")
    personas = cursor.fetchone()
    if personas != None:
        if personas[6] != 0:
            valor = messagebox.askokcancel("ELiminar",f"desea eliminar{ personas[2] , personas[3]}?") #y esat la opcion de aceptar o cancelar
            if valor == True:
                cursor.execute("UPDATE Persona SET VISUAL = 0 WHERE ID = '"+str(id)+"'")
        else:
            valor = messagebox.askokcancel("Obtener",f"{ personas[2] , personas[3]} ya estas eliminado , quiere agregarlo otra vez ?") #y esat la opcion de aceptar o cancelar
            if valor == True:
                cursor.execute("UPDATE Persona SET VISUAL = 1 WHERE ID = '"+str(id)+"'")
    else : 
        messagebox.showwarning("Persona no encontrada", "no existe una persona con el id " + str(id))
    
    Conexion.commit()

def ActualizarPersona(id , num , Nuevo_dato):
    if ExisteLaPersona(id) == True:
        Conexion = sqlite3.connect("Prueba_Grafica_BBDD")
        cursor = Conexion.cursor()
        if num == 1 :
            cursor.execute("UPDATE Persona SET NOMBRE = '"+ str(Nuevo_dato) +"' WHERE ID = '"+str(id)+"'")  
        elif num == 2:
            cursor.execute("UPDATE Persona SET APELLIDO = '"+ Nuevo_dato +"' WHERE ID = '"+ str(id)+"'")
        elif num == 3:
            cursor.execute("UPDATE Persona SET DNI = '"+ Nuevo_dato +"' WHERE ID = '"+ str(id)+"'")
        elif num == 4:
            cursor.execute("UPDATE Persona SET GMAIL = '"+ Nuevo_dato +"' WHERE ID = '"+ str(id)+"'")
        elif num == 5:
            cursor.execute("UPDATE Persona SET AÑO_DE_NACIMIENTO = '"+ Nuevo_dato +"' WHERE ID = '"+ str(id)+"'")
        Conexion.commit()
        return True
    else:
        return False

def MostrarNoEliminados():
    Conexion = sqlite3.connect("Prueba_Grafica_BBDD")
    cursor = Conexion.cursor()
    cursor.execute("SELECT ID , NOMBRE , APELLIDO , GMAIL FROM Persona WHERE VISUAL == 1")
    personas = cursor.fetchall()
    return personas

def MostrarELiminados():
    Conexion = sqlite3.connect("Prueba_Grafica_BBDD")
    cursor = Conexion.cursor()
    cursor.execute("SELECT ID , NOMBRE , APELLIDO , GMAIL FROM Persona WHERE VISUAL == 0")
    personas = cursor.fetchall()
    return personas

def ExisteLaPersona(id):
    Conexion = sqlite3.connect("Prueba_Grafica_BBDD")
    cursor = Conexion.cursor()
    cursor.execute("SELECT * FROM Persona WHERE ID == '"+ str(id) +"'")
    personas = cursor.fetchone()
    if personas != None:
        return True
    else:
        messagebox.showwarning("Persona no encontrada", "no existe una persona con el id " + str(id))
        return False