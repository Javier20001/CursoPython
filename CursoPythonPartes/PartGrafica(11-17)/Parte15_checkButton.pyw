


from tkinter import *


root = Tk()
root.title("checkbutton")
varPlaya = IntVar()
varMontaña = IntVar()
varBosque= IntVar()
varTexto = StringVar()

def opcion():
    if varPlaya.get()==1:
        varTexto.set(varTexto.get()+"Eligio la playa")
    elif varMontaña.get()==1:
        varTexto.set(varTexto.get()+"Eligio montaña")
    elif varBosque.get()==1:
        varTexto.set(varTexto.get()+"Eligio el Bosque")
    
    textoFinal.config(text=varTexto.get())


frame  = Frame(root,width=100,height=40).pack()

Checkbutton(frame,text="Playa",variable=varPlaya,onvalue=1,offvalue=0,command=lambda:opcion()).pack()
Checkbutton(frame,text="Montaña",variable=varMontaña,onvalue=1,offvalue=0,command=lambda:opcion()).pack()
Checkbutton(frame,text="Bosque",variable=varBosque,onvalue=1,offvalue=0,command=lambda:opcion()).pack()

textoFinal = Label(frame).pack()

root.mainloop()