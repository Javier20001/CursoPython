from distutils import command
from tkinter import *
from tkinter import filedialog


root = Tk()
def abrirFichero():
    fichero = filedialog.askopenfilename(title="open file",initialdir="C:",filetypes=(("ficheros exel","*.xlsx"),
    ("Ficheros text","*.txt"),("todos Los ficheros","*.*")))

    print(fichero)


Button(root , text="open File",command=lambda:abrirFichero()).pack()

root.mainloop()