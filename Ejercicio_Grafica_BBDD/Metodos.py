import tkinter
from tkinter import messagebox

#---- data base modulo
from Parte_BBDD import * 
import Main

from re import fullmatch
ListaP = []
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'


def salir(root):#funcion para salir
    valor = messagebox.askquestion("Salir","¿Realmente desea salir de la aplicacion?") #da la opcion de si o no 
    if valor == "yes":
        root.destroy()

def MostrarPersonas(Tabla):
    BorrarLista(Tabla)
    ListaP = MostrarNoEliminados()
    for i in range(len(ListaP)):
        Tabla.insert(parent='',index='end',iid=i,text='',values=ListaP[i])

def MostrarPersonasELiminadas(Tabla):
    BorrarLista(Tabla)
    ListaP = MostrarELiminados()
    for i in range(len(ListaP)):
        Tabla.insert(parent='',index='end',iid=i,text='',values=ListaP[i])

def BorrarLista(Tabla):
    for i in Tabla.get_children():
        Tabla.delete(i)
    ListaP.clear()

def EnviarAlCrear(Nombre , Apellido , Gmail ,Fecha ,Dni ):#le enviamos los datos al INSERT INTO
    if len(Nombre)!=0 and len(Apellido)!=0 and len(Gmail)!=0 and len(Fecha)!=0 and len(Dni)!=0 :
        if checkNombreyApellido(Nombre) == False and checkNombreyApellido(Apellido) == False:
            if check(Gmail):
                if checkDni(Dni):
                    CrearPersona(Nombre , Apellido , Gmail ,Fecha ,Dni)
                    
                    return True 
                else:
                    messagebox.showwarning("Error_DNI_invalido","EL DNI solo debe llevar numeros o esta incompleto")
            else:
                messagebox.showwarning("Error_gmail_invalido","El Gmail esta incompleto o erroneo")
        else:
            messagebox.showwarning("Error_Nombre_Apellido","EL nombre o el apellido tienen digitos ")
    else:
        messagebox.showwarning("Ausencia de datos","falta casillas por llenar")
    return False
    
def check(gmail):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (fullmatch(regex,gmail)):
        return True
    else:
        return False

def checkNombreyApellido(palabra):
    if palabra.isdigit():
        return True
    else:
        return False

def checkDni(DNI):
    if DNI.isdigit() and len(DNI) == 8:
        return True
    else:
        return False

