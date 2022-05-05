#----------------GENERADORES-----------------
"""
import random


def generatorNumber(limit):
    num = 1
    while num <= limit:
        yield random.randint(1,100) #lo que hace yield es almacenar valores en una lista y retornarlo dependiendo de cuantas veces llamemos a la funcion 
        num = num + 1 

numbersList = generatorNumber(10)#entonces en esta variables se va guardar una lista generada por la funcion 


print(next(numbersList))#hay algo interesante en esto y es que las veces que llamemos a la variable sera cuando cree los numero 
#por ejemplo , con next solo estamos imprimiendo el primer valor , pero es todo lo que existe , no hay mas ....
print(next(numbersList))#ahora existe un segundo valor dentro de esa lista...

print(next(numbersList))#ahora un tercero y asi sucesivamente hasta que lleguemos al final de la lista
"""

from ast import YieldFrom


def cityGenerator(*citys):#cuando usamos el * cuando psamos parametros indicamos que pasaramenos un numero inexsacto de parametros
    for i in citys:
        yield i 

#citysList = cityGenerator("argentina" , "madrid" , "italia")


#hasta aqui nada nuevo le pasamos por parametros los valores y crea una lista , imagina ahora que solo queremos las letras en vez de la palbra completa , bueno ....

def cityGenerator2(*citys):
    for i in citys: 
        #for j in i: #aunque hay una forma de hacer mas facil esto que con un bucle añidado , y es con : yieldFrom
        yield from i #esto nos dara el mismor resultado : "a r g"

citysList = cityGenerator2("argentina" , "madrid" , "italia")

print(next(citysList))
print(next(citysList))
print(next(citysList))

