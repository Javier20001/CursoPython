#import tkinter
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext



#---- data base modulo
from Parte_BBDD import *
#---- create modulo
from CrearGrafico import *
#---- delete modulo
from EliminarGrafico import *
#--- upgrade modulo
from AcutializarGrafico import *
#--- Metodos modulo
from Metodos import *

def iniciar(ventanaPadre):

    ventanaPadre.withdraw()
    ventanaHija = Toplevel(ventanaPadre)
    barraMenu = Menu(ventanaHija)
    ventanaHija.config(menu=barraMenu)
    ventanaHija.resizable(0,0)
    ventanaHija.title("Programa de Personas")


    #------------ Creacion de frames ---------------
    frame1 = Frame(ventanaHija,width=200,height=400,bg="#8d9c96")
    frame2 = Frame(ventanaHija ,width=600,height=400,bg="#eb366c")
    frame3 = Frame(ventanaHija,width=400,height=2,bg="#eb366c")
    frame1.pack(side="left",fill="both",expand=False)
    frame3.pack(fill="both",expand=True)
    frame2.pack(fill="both",expand=True)


    #--------------Frame1--------------
    Button(frame1,text="Crear",command=lambda:IngresarDatosPersona(my_game,ventanaHija),width=10).pack(side="top",padx=10,pady=30)#.grid(row=0,column=1,padx=8,pady=30)
    Button(frame1,text="Eliminar",width=10,command=lambda:IngresarIDparaELiminar(my_game,ventanaHija)).pack(side="top",padx=10)#.grid(row=1,column=1,padx=8,pady=30)
    Button(frame1,text="Actulizar",width=10,command=lambda:EleccionParaActualizar(my_game,ventanaHija)).pack(side="top",padx=10,pady=30)#.grid(row=2,column=1,padx=8,pady=30)

    #--------------Frame2-------------
    my_game = ttk.Treeview(frame2)

    my_game['columns'] = ('Persona_id', 'Persona_name', 'Persona_apellido', 'Persona_Gmail')

    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Persona_id",anchor=CENTER, width=80)
    my_game.column("Persona_name",anchor=CENTER,width=80)
    my_game.column("Persona_apellido",anchor=CENTER,width=80)
    my_game.column("Persona_Gmail",anchor=CENTER,width=180)

    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("Persona_id",text="Id",anchor=CENTER)
    my_game.heading("Persona_name",text="Name",anchor=CENTER)
    my_game.heading("Persona_apellido",text="Apellido",anchor=CENTER)
    my_game.heading("Persona_Gmail",text="GMAIL",anchor=CENTER)

    my_game.pack()
    
    #--------------Frame3---------------
    MostrarPersonas(my_game)
    Button(frame3,text="SIN ELIMINAR",width=10,command=lambda:MostrarPersonas(my_game)).pack(side="left",pady=5 ,padx= 5)
    Button(frame3,text="ELIMINADOS",width=10,command=lambda:MostrarPersonasELiminadas(my_game)).pack(side="left",pady=5)

    #--------------MENU PART-------
    Archivo_menu = Menu(barraMenu , tearoff = 0)
    barraMenu.add_cascade(label="Archivo", menu=Archivo_menu)
    Archivo_menu.add_command(label="Salir",command=lambda:salir(ventanaHija))#salir de la aplicacion

    ventanaHija.mainloop()

