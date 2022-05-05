from tkinter import *
from tkinter import messagebox
from Parte_BBDD import *
from Metodos import * 

def IngresarIDparaELiminar(scrText,ventanaPadre):
    root = Toplevel(ventanaPadre)
    root.geometry('250x90+300+300')

    IDnumero = IntVar()
    def Remove_in_the_table():
        EliminarPersona(IDnumero.get())
        IDnumero.set(0)
        MostrarPersonas(scrText)

    frame1  = Frame(root)
    frame2  = Frame(root)
    frame1.pack(fill="both",expand=False)
    frame2.pack(fill="both",expand=False)
    Label(frame1,text = "Inserte el ID de la persona").grid(row=0 , column=0)
    Entry(frame1, textvariable= IDnumero).grid(row=0,column=1)
    Button(frame2 , text = "Eliminar", command= lambda:Remove_in_the_table()).pack(side="top",pady=10)

    root.mainloop()

