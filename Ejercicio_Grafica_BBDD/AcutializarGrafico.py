from tkinter import *
from tkinter import messagebox
from Parte_BBDD import *
from Metodos import *

def EleccionParaActualizar(scrText,ventanaPadre):
    ventaNieta = Toplevel(ventanaPadre)
    ventaNieta.geometry('150x250+300+300')

    IDnumero = IntVar()

    frame1  = Frame(ventaNieta)
    frame1.pack(fill="both",expand=False)
    
    Label(frame1,text = "Inserte el ID de la persona").pack(side="top",pady=5)
    Entry(frame1, textvariable= IDnumero).pack(side="top",pady=5)
    Button(frame1 , text = "NOMBRE",command=lambda:IngresoParaActualizar(1,IDnumero.get(),scrText,ventaNieta)).pack(side="top",pady=5)
    Button(frame1 , text = "APELLIDO",command=lambda:IngresoParaActualizar(2,IDnumero.get(),scrText,ventaNieta)).pack(side="top",pady=5)
    Button(frame1 , text = "DNI",command=lambda:IngresoParaActualizar(3,IDnumero.get(),scrText,ventaNieta)).pack(side="top",pady=5)
    Button(frame1 , text = "GMAIL",command=lambda:IngresoParaActualizar(4,IDnumero.get(),scrText,ventaNieta)).pack(side="top",pady=5)
    Button(frame1 , text = "FECHA",command=lambda:IngresoParaActualizar(5,IDnumero.get(),scrText,ventaNieta)).pack(side="top",pady=5)

    ventaNieta.mainloop()

def IngresoParaActualizar(num,ID,scrText,ventanaPadre):
    if ExisteLaPersona(ID):
        ventanaBisnieta = Toplevel(ventanaPadre)
        ventanaBisnieta.geometry('250x100+300+300')

        frame1  = Frame(ventanaBisnieta)
        frame1.pack(fill="both",expand=False)
        auxVar = StringVar()

        def EnviarAlActualizar(ID,num):
            if ActualizarPersona(ID,num,auxVar.get()) == True:
                auxVar.set("")
                MostrarPersonas(scrText)

        if num == 1:
            Label(frame1,text = "Inserte el nuevo Nombre de la persona").pack(side="top",pady=5)
            Entry(frame1, textvariable=auxVar ).pack(side="top",pady=5)
            Button(frame1 , text = "CAMBIAR",command=lambda:EnviarAlActualizar(ID,1)).pack(side="top",pady=5)
        if num == 2:
            Label(frame1,text = "Inserte el nuevo Apellido de la persona").pack(side="top",pady=5)
            Entry(frame1, textvariable=auxVar).pack(side="top",pady=5)
            Button(frame1 , text = "CAMBIAR",command=lambda:EnviarAlActualizar(ID,2)).pack(side="top",pady=5)
        if num == 3:
            Label(frame1,text = "Inserte el nuevo DNI de la persona").pack(side="top",pady=5)
            Entry(frame1, textvariable=auxVar).pack(side="top",pady=5)
            Button(frame1 , text = "CAMBIAR",command=lambda:EnviarAlActualizar(ID,3)).pack(side="top",pady=5)
        if num == 4:
            Label(frame1,text = "Inserte el nuevo GMAIL de la persona").pack(side="top",pady=5)
            Entry(frame1, textvariable=auxVar).pack(side="top",pady=5)
            Button(frame1 , text = "CAMBIAR",command=lambda:EnviarAlActualizar(ID,4)).pack(side="top",pady=5)
        if num == 5:
            Label(frame1,text = "Inserte la Fecha de la persona").pack(side="top",pady=5)
            Entry(frame1, textvariable=auxVar).pack(side="top",pady=5)
            Button(frame1 , text = "CAMBIAR",command=lambda:EnviarAlActualizar(ID,5)).pack(side="top",pady=5) 

        ventanaBisnieta.mainloop()
