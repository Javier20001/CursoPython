from re import T
from tkinter import * 

raiz = Tk()#la raiz es la pantalla en blanco de la interfaz 

raiz.title("Primera vernta")
raiz.resizable(1,1)#0 no deja cambiar tamaño,1 si lo hace.en este caso podemos agrandar el alto pero no el ancho 
#raiz.iconbitmap("yatta.ico")#PARA CAMBIAR EL LOGO 
#raiz.geometry("400x500")#esto le dara tamño a la raiz , pero la raiz debe adaptarse al frame entonces al que debemos daarle tamaño es al frame

raiz.config(bg="purple")

myframe = Frame()#los frame sos donde se colocaran las heramientas de la interfaz 
myframe.pack(side="left",anchor="n",fill="both",expand=True)#podemos alterar el posicionamiento con side = "left" ,"right ", "top" y "bottom" 
#el parametro side lo prondra en el medio de la posicion , tambien le podemos indicar en que esquina puede estar
#con el parametro anchor = "n","s","e","w" 
#tambien se podemos rellenar el espacio con fill = "x"(re llena en el eje x),"y"(rellana en el eje y siempre que este expand =True),"both"(rellana en ambas direcciones usando tambien el exapand = True)
myframe.config(bg="red",width="300",height="200")#control de ancho y alto

myframe.config(relief="solid",bd=5)#cambia el marquito(flat, groove, raised, ridge, solid, or sunken) y el bd le da un grosor

myframe.config(cursor="hand2")#cambia el cursor
raiz.mainloop()#esto siempre a lo ultimo 