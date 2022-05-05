import pickle
from time import perf_counter
"""
#lo que haremos hoy con la serializacion es guardar datos en memoria biniaria 
ListaNombres = ["pedro","Maria","Ana","Isabel"]#vamos a volcar la lsita en un fichero para guardarlo de forma binaria

ficheroBinario = open("ListaNombres","wb")#la "b" de wb es de bites , tambien se debe usar para el "read"

pickle.dump(ListaNombres,ficheroBinario)#y eso lo hacemo con el metodo dump 

ficheroBinario.close()#cerramos 

del(ficheroBinario)#y el fichero podemos eliminarlo de la memoria ya que la lista esta guardada de forma binaria en el disco y no en el fichero 
#asi que uno no afectara al otro 


fichero = open("ListaNombres","rb")#abrimos un nuevo fichero y le idicamos que abra el archivo "ListaNombre"

listaN = pickle.load(fichero)#para leer los datos que estan guardados de forma binaria necesitamos el load()
#ahora la variable lista contiene los datos que almaceno de forma binaria el fichero que contenia una lista de nombres
print(listaN)
"""
#-----------------Serializar objetos----------------
import pickle

class Persona():
    def __init__(self,n,a,s) :
        self.__name = n 
        self.__age = a 
        self.__size = s
    
    def talk(self):
        print("hi , my name is " ,self.__name, " and i have " ,self.__age, "age old")

    def walk(self):
        print("im walking")

Persona1 = Persona("Lucho",25,1.75)
Persona2 = Persona("Faqu",22,1.65)
Persona3 = Persona("Cesar",22,1.68)

listaobjetos = [Persona1,Persona2,Persona3]

fichero = open("ListaObjetos","wb")

pickle.dump(listaobjetos,fichero)

fichero.close()

del(fichero)

fichero = open("ListaObjetos","rb")

ListaPersona = pickle.load(fichero)

fichero.close()


for p in ListaPersona:
    p.talk()




