from tkinter import * 
from Main import * 
from Metodos import *  

ventanPadre = Tk()
ventanPadre.title("Loging")
ventanPadre.geometry("400x200")
ventanPadre.resizable(0,0)

def conectar_iniciar(root):#funtion for conect whit de data base
    conectar()
    iniciar(root)

#------Frame's Part
frame1 = Frame(ventanPadre,bg="#eb366c")
frame1.pack(fill="both",expand=True)

#-------buttom's part
Button(frame1,text="conectar",width=20,command=lambda:conectar_iniciar(ventanPadre)).pack(side="top",pady=30)
Button(frame1,text="salir",command=lambda:salir(ventanPadre),width=20).pack(side="top",pady=30)

ventanPadre.mainloop()