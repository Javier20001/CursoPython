from asyncio.windows_events import NULL
import pickle
from weakref import finalize

class Persona():
    def __init__(self,n,a,s,g) :
        self.__name = n 
        self.__age = a 
        self.__size = s
        self.__genero = g
    
    def talk(self):
        print("hi im a " ,self.__genero , "my name is " ,self.__name, " and i have " ,self.__age, "age old")

    def __str__(self):
        return "{}{}{}{}".format(self.__name,self.__age,self.__size,self.__genero)

class ListaPersonas():
    listaPersonas = []

    def AgregarPersonas(self , P):
        self.listaPersonas.append(P)

    def LeerPersonas(self):
        for p in self.listaPersonas:
            p.talk()

    def getLista(self):
        return self.listaPersonas
    
class Archivos():
    def __init__(self,nombre):
        self.__Nombre = nombre

    def Escribir(self,contenido):
        fichero= open(self.__Nombre,"wb")
        pickle.dump(contenido,fichero)
        print("agregado con exito")
        fichero.close()
        del(fichero)

    def Leer(self):
        Fichero = open(self.__Nombre,"rb+")
        almacen = pickle.load(Fichero)
        
        Fichero.close()
        del(Fichero)

        for i in almacen:
            i.talk()



Lista1 = ListaPersonas()

p1 = Persona("sandra",18,1.76,"female")
p2 = Persona("Cesar",21,1.67,"male")
p3 = Persona("Mirta",64,1.70,"female")

f1 = Archivos("ListaPersonas")

Lista1.AgregarPersonas(p1)
Lista1.AgregarPersonas(p2)
Lista1.AgregarPersonas(p3)

listaPersonas = Lista1.getLista()

f1.Escribir(listaPersonas)
f1.Leer()