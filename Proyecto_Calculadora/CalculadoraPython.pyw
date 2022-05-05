from tkinter import *
from tkinter import messagebox

#root create
root = Tk()

num1_var = StringVar()
aux_var = IntVar()
sim_var = IntVar()


#funtion's

def Borrar():
    num1_var.set("")
    sim_var = 0

def Suma():
    n1 = aux_var.get()
    n2 = int(num1_var.get())
    messagebox.showinfo("Resultado",n1+n2)
    num1_var.set(n1+n2)
    aux_var.set(0)

def Resta():
    n1 = aux_var.get()
    n2 = int(num1_var.get())
    messagebox.showinfo("Resultado",n1-n2)
    num1_var.set(n1-n2)
    aux_var.set(0)

def Multiplicar():
    n1 = aux_var.get()
    n2 = int(num1_var.get())
    messagebox.showinfo("Resultado",n1*n2)
    num1_var.set(n1*n2)
    aux_var.set(0)

def Dividir():
    try:    
        n1 = aux_var.get()
        n2 = int(num1_var.get())
        if n1>0:   
            messagebox.showinfo("Resultado",round(n1/n2))
            num1_var.set(round(n1/n2))
            aux_var.set(0)
        else:
            t="El resultado es 0"
            messagebox.showinfo("Resultado",t)
            num1_var.set()
            aux_var.set(0)    
    except:
        t = "No se puede dividir por 0"
        messagebox.showinfo("ERROR",t)
        num1_var.set(0)
        aux_var.set(0)

def Resultado():
    if sim_var.get() == 1:
        Suma() 
    elif sim_var.get() == 2:
        Resta()
    elif sim_var.get() == 3:
        Multiplicar()
    elif sim_var.get() == 4:
        Dividir()
    else:
        t="0"
        messagebox.showinfo("Resultado",t)
    
def Seleccion(n):
    sim_var.set(n)
    try:
        aux_var.set(int(num1_var.get()))
        Borrar()

    except:
        t = "No se puede sumar sin ingresar los numeros"
        messagebox.showinfo("ERROR",t)
    
def imprimir(n):
    num1_var.set(num1_var.get()+n)

#frames part 
frame1 =  Frame(root,width=200,height=300)
frame2 = Frame(root ,width=200,height=300,bg="#8d9c96")
frame3 = Frame(root,width=200,height=100,bg="#55602d")

frame2.pack(side="right",fill="both",expand=True)
frame1.pack(side="top",fill="both",expand=True)
frame3.pack(side="bottom",fill="both",expand=True)

pantalla = Entry(frame1,width=15,textvariable=num1_var).grid(row=0,column=0,padx=20,pady=10)

#----------------botones operadores-----------
Button(frame2,text="C",command=lambda:Borrar(),width=5).grid(row=0,column=0,padx=4)
Button(frame2,text="+",command=lambda:Seleccion(1),width=5).grid(row=1,column=0,padx=4)
Button(frame2,text="-",command=lambda:Seleccion(2),width=5).grid(row=2,column=0,padx=4)
Button(frame2,text="*",command=lambda:Seleccion(3),width=5).grid(row=3,column=0,padx=4)
Button(frame2,text="/",command=lambda:Seleccion(4),width=5).grid(row=4,column=0,padx=4)
Button(frame2,text="=",command=lambda:Resultado(),width=5).grid(row=5,column=0,padx=4)

#----------------------botones numericos------------
Button(frame3,text="1",command=lambda:imprimir("1"),width=4).grid(row=0,column=0,padx=4,pady=2)
Button(frame3,text="2",command=lambda:imprimir("2"),width=4).grid(row=0,column=1,padx=4,pady=2)
Button(frame3,text="3",command=lambda:imprimir("3"),width=4).grid(row=0,column=2,padx=4,pady=2)
Button(frame3,text="4",command=lambda:imprimir("4"),width=4).grid(row=1,column=0,padx=4,pady=2)
Button(frame3,text="5",command=lambda:imprimir("5"),width=4).grid(row=1,column=1,padx=4,pady=2)
Button(frame3,text="6",command=lambda:imprimir("6"),width=4).grid(row=1,column=2,padx=4,pady=2)
Button(frame3,text="7",command=lambda:imprimir("7"),width=4).grid(row=2,column=0,padx=4,pady=2)
Button(frame3,text="8",command=lambda:imprimir("8"),width=4).grid(row=2,column=1,padx=4,pady=2)
Button(frame3,text="9",command=lambda:imprimir("9"),width=4).grid(row=2,column=2,padx=4,pady=2)
Button(frame3,text="0",command=lambda:imprimir("0"),width=4).grid(row=3,column=1,padx=4,pady=2)

root.mainloop()