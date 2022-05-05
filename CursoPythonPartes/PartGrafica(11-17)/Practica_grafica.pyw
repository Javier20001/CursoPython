
from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import scrolledtext as st


#------------vetana
root = Tk()

#------------variables al pedo----------
nam_var = StringVar()
secondNam_var = StringVar()
direction_var = StringVar()


#------------funciones al pedo----------
def AgregarValores():

    nombre = nam_var.get()
    apellido = secondNam_var.get()
    direccion = direction_var.get()

    print("Este es tu nombre:  "+nombre)
    print("Este es tu apellido:  "+apellido)
    print("Esta es tu direccion:  "+direccion)
    
    nam_var.set("")
    secondNam_var.set("")
    direction_var.set("")


#-------------frames
frame1 = Frame(root,width="200",height="300",bg="#8d9c96")
frame2 = Frame(root,width="100",height="300",bg="#7af5c3")
frame1.pack(side="left",fill="both",expand=True)
frame2.pack(fill="both",expand=True)


#------------------Labels al pedo----------
Label(frame1,text = "Nombre",bg="#8d9c96").grid(row=0,column=0,sticky="e",pady=2,padx=8)
Label(frame1,text = "Apellido",bg="#8d9c96").grid(row=1,column=0,sticky="e",pady=2,padx=8)
Label(frame1,text = "Direccion",bg="#8d9c96").grid(row=2,column=0,sticky="e",pady=2,padx=8)

Label(frame2,text="introduzca un comentario de 20 palabras",bg="#7af5c3").grid(row=0,column=0,sticky="w",pady=2,padx=8)

#----------------------Entrys al pedo---------
Entry(frame1,textvariable=nam_var).grid(row=0,column=1,padx=6)
Entry(frame1,textvariable=secondNam_var).grid(row=1,column=1,padx=6)
Entry(frame1,textvariable=direction_var).grid(row=2,column=1,padx=6)

#----------------------Texto al pedo-------------
#ScrolledText(frame2,width=30,height=10,).grid(row=1,column=0,padx=10,pady=5)
Lista_Nombres = [("maria","juan","carlos"),("juan","maria","carlos"),("maria","carlos","juan")]
#Lista_separacion = 
textodelst1 = st.ScrolledText(frame2,width=30,height=10)
for i in Lista_Nombres:
    print(i)
    textodelst1.insert(tkinter.INSERT,f"{i}\n")
textodelst1.config(state="disabled")
textodelst1.grid(row=1,column=0,padx=10,pady=5)

#----------------Botones al pedo
botom1 = Button(frame1 ,text="Mostrar",command=AgregarValores).grid(row=4,column=1)



root.mainloop()