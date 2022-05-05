from tkinter import *
from tkinter import messagebox
from Parte_BBDD import *
from Metodos import * 



def IngresarDatosPersona(scrText , ventanPadre):
    nombre = StringVar()
    apellido = StringVar()
    gmail = StringVar()
    fecha = StringVar()
    dni = StringVar()

    root = Toplevel(ventanPadre)
    root.geometry('250x150+300+300')

    def EnviarAlCrearGrafico():
        if EnviarAlCrear(nombre.get() , apellido.get() , gmail.get() ,fecha.get() ,dni.get()):
            nombre.set("")
            apellido.set("")
            gmail.set("")
            fecha.set("")
            dni.set("")
            MostrarPersonas(scrText)

    #creamos los frames
    frame1 = Frame(root,width=250,height=300)
    frame2 = Frame(root,width=250,height=40)
    frame1.pack(fill="both",expand=False)
    frame2.pack(fill="both",expand=True)

    Label(frame1,text="Nombre").grid(row=0,column=0,padx=10)
    Label(frame1,text="Apellido").grid(row=1,column=0)
    Label(frame1,text="DNI").grid(row=2,column=0)
    Label(frame1,text="FECHA DE NACIMIENTO").grid(row=3,column=0,sticky="w")
    Label(frame1,text="GMIAL").grid(row=4,column=0)

    Entry(frame1,textvariable=nombre).grid(row=0,column=1,sticky="w")
    Entry(frame1,textvariable=apellido).grid(row=1,column=1,sticky="w")
    Entry(frame1,textvariable=dni).grid(row=2,column=1,sticky="w")
    Entry(frame1,textvariable=fecha).grid(row=3,column=1,sticky="w")
    Entry(frame1,textvariable=gmail).grid(row=4,column=1,sticky="w")

    Button(frame2,text="Crear",command=lambda:EnviarAlCrearGrafico()).pack(side="top",pady=10)

    root.mainloop()