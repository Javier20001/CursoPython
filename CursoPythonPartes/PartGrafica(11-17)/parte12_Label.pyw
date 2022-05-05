
from tkinter import *
 
root = Tk()
root.title("Programa")
#root.iconbitmap("yatta.ico")
primerFrame= Frame(root,width="200",height="300",bg="#8d9c96")
segundoFrame = Frame(root,width="100",height="300",bg="#7af5c3")
primerFrame.pack(side="left",anchor="n",fill="both",expand=True)
segundoFrame.pack(fill="both",expand=True)

primerLabel = Label(primerFrame, text="hola putos")
#primerLabel.pack()#si usamos el label y lo colocamos en el pack , el frame se va adapapta al label , entonces nos va quedar chiquito 
#y no respetara las medidas del frame 
primerLabel.place(x=0,y=0)#posicionamiento del label 

#tambien podemos descartar la la construcion del label y solo usar el metodo constructor "Label"
Label(primerFrame, text="chau trolos").place(x=0,y=20)#como ven no declaromo un segundo label y solo usamos los metodos
Label(primerFrame, text="que tal estan",fg="#2e6417",font=("Comic Sans MS",16)).place(x=0,y=70)#el fg alreta el color , el font altera el tamaño y la fuente

#para mostrar imagenes debemos 
#primerImagen = PhotoImage(file="rose.png") creamos una variale que tiene la imagen
#Label(primerFrame, image=primerImagen).place(x=20,y=80) y se la pasamos a un label 
primerFrame.mainloop()