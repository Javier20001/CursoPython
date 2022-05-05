
from tkinter import *


root = Tk()

varOpcion = IntVar()

def imprimir():
    
    if varOpcion.get() == 1:
        print("Masculino")
    elif varOpcion.get() == 2:
        print("Femenino")
    
frame = Frame(root,width=100,height=30).pack()

Radiobutton(frame,text="Masculino",variable=varOpcion,value=1,command=lambda:imprimir()).pack()
Radiobutton(frame,text="Fememnino" ,variable=varOpcion,value=2,command=lambda:imprimir()).pack()

root.mainloop()