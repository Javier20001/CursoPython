from tkinter import *
from  tkinter import ttk
#import pil
from Parte_BBDD import * 

k = 0

ws  = Tk()

game_frame = Frame(ws)
buttons_frames = Frame(ws)
game_frame.pack(side="right")
buttons_frames.pack()
my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('Persona_id', 'Persona_name', 'Persona_apellido', 'Persona_Gmail','Persona_opcion')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("Persona_id",anchor=CENTER, width=80)
my_game.column("Persona_name",anchor=CENTER,width=80)
my_game.column("Persona_apellido",anchor=CENTER,width=80)
my_game.column("Persona_Gmail",anchor=CENTER,width=180)
my_game.column("Persona_opcion",anchor=CENTER, width=80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("Persona_id",text="Id",anchor=CENTER)
my_game.heading("Persona_name",text="Name",anchor=CENTER)
my_game.heading("Persona_apellido",text="Apellido",anchor=CENTER)
my_game.heading("Persona_Gmail",text="GMAIL",anchor=CENTER)
my_game.heading("Persona_opcion",text="",anchor=CENTER)

ListaP = MostrarNoEliminados()
photoCrear = PhotoImage(file = r"C:\Users\kuzni\OneDrive\Escritorio\facultad\cursoPython\PartGrafica\OIP.png") 
photoELiminar = PhotoImage(file = r"C:\Users\kuzni\OneDrive\Escritorio\facultad\cursoPython\PartGrafica\TachoBasura.png") 
photoimage = photoCrear.subsample(10, 10) 
photoimage2 = photoELiminar.subsample(30, 30) 

#ListaB = [botom]
for i in range(len(ListaP)):
    """nuevaLista = list(ListaP[i])
    resultado = nuevaLista + ListaB
    my_game.insert(parent='',index='end',iid=i,text='',values=resultado)
    """
    botom = Button(buttons_frames,width=10,image = photoimage).grid(row=k,column=0)
    botom = Button(buttons_frames,width=10,image= photoimage2).grid(row=k,column=1)
    my_game.insert(parent='',index='end',iid=i,text='',values=ListaP[i])
    k += 1
    

my_game.pack()

ws.mainloop()

