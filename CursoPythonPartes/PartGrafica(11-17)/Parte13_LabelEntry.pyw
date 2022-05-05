from pydoc import text
from tkinter import *
from unittest import TestCase

root = Tk()

frame1 = Frame(root,width="200",height="300",bg="#8d9c96")
frame2 = Frame(root,width="100",height="300",bg="#7af5c3")
frame1.pack(side="left",anchor="n",fill="both",expand=True)
frame2.pack(fill="both",expand=True)
cuadroTexto = Entry(frame1)#cramos el primer cuadro para insertar texto  y lo metemos en el primer frame
#cuadroTexto.place(x=0,y=0)#le damos pocicionamiento


#imaginemos que quermos hacer un cuestionario , para esto vamos usar el metodo grid
#esto nos permitira colocar los componentes (label , entry , etc) de forma concreta y prolija 
cuadroTexto.grid(row=0,column=1,sticky="w")#entonces esto hara una grilla y colocara los elementos donde le indiquemos
#tambien podemos llamar al metodo cuando lo creamos : "cuadroTexto = Entry(frame1,text="introdusca su nombre").grid(row=0,column=1)"
texto = Label(frame1,text = "Nombre",bg="#8d9c96").grid(row=0,column=0,sticky="w",pady=2)#creamos un label que contenga un "nombre"

Label(frame1,text = "Apellido",bg="#8d9c96").grid(row=1,column=0,sticky="w",pady=2)#con sticky indicamos el posicionamiento 
Entry(frame1).grid(row=1,column=1)

Label(frame1,text = "Direccion de Correo Electronico",bg="#8d9c96").grid(row=2,column=0,sticky="e",pady=2)
Entry(frame1).grid(row=2,column=1)



root.mainloop()