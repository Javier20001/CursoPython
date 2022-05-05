from tkinter import *
from tkinter import messagebox

root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu)

def MensajeAyuda():
    messagebox.showinfo("Centro de ayuda","Puede contactartar con el administrador al: ")

def MensajeAdbertencia():
    messagebox.showwarning("Estado de Liscencia", f"En los sigueintes {40} dias tendra que renovar su Licencia")

def CerrarAplicacion():
    """valor = messagebox.askquestion("Salir","¿Realmente desea salir de la aplicacion?") #da la opcion de si o no 
    if valor == "yes":
        root.destroy()"""
    valor = messagebox.askokcancel("Salir","¿Realmente desea salir de la aplicacion?") #y esat la opcion de aceptar o cancelar
    if valor == True:
        root.destroy()

def ReintentarCerrar():
    valor = messagebox.askretrycancel("Cerrar","no se logro cerrar")
    if valor == True:
        root.destroy()




ArchivoMenu = Menu(barraMenu , tearoff= 0)
barraMenu.add_cascade(label="Archivo",menu=ArchivoMenu)
ArchivoMenu.add_command(label="Nuevo")
ArchivoMenu.add_command(label="Abrir")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label="Guardar")
ArchivoMenu.add_command(label="Guardar Como")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label="Cerrar",command=lambda:ReintentarCerrar())
ArchivoMenu.add_command(label="Salir",command=lambda:CerrarAplicacion())

EdicionMenu = Menu(barraMenu , tearoff= 0)
barraMenu.add_cascade(label="Edicion",menu=EdicionMenu)
EdicionMenu.add_command(label="Paso adelante")
EdicionMenu.add_command(label="Paso Atras")
EdicionMenu.add_command(label="Pegar")
EdicionMenu.add_command(label="Copiar")


HerramientaMenu = Menu(barraMenu , tearoff= 0)
barraMenu.add_cascade(label="Herramienta",menu=HerramientaMenu)


HelpMenu = Menu(barraMenu , tearoff= 0)
barraMenu.add_cascade(label="Help",menu=HelpMenu)
HelpMenu.add_command(label="Licencia",command=lambda:MensajeAdbertencia())
HelpMenu.add_command(label="Ayuda",command=lambda:MensajeAyuda())

#barraMenu.add_cascade(label="Archivo",menu=ArchivoMenu)
#barraMenu.add_cascade(label="Edicion",menu=EdicionMenu)
#barraMenu.add_cascade(label="Herramienta",menu=HerramientaMenu)
#barraMenu.add_cascade(label="Help",menu=HelpMenu)

root.mainloop()