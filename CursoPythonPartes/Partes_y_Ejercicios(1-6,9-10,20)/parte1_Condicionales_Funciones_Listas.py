#print("hello world") making a print in console 
#print("Hola mundo");print("adios mundo") in this way, use the ; for conect two sentence 
mi_Nombre="Mi nombre es javier" #like this we create a varible and give he a valor 
mi_Nombre #if i call he like that , go to print in the terminal the valor he has 
#also with a \ can do a jump line , like this:
#mi_Nombre_completo = "mi nombre completo es\
# javier alejandro kuznik" #the sentence still working like a normal line code only now it's divide

#print(mi_Nombre_completo)

a = 4+5
b = 10%3
c = 5**3 #5 elevado a 3 que da 125
d = 9//2 #divide y nos da un entero 
#print(d)


numero = 5 
#print(type(numero)) #the function type show us the data type of the varible we choise , in this case is "numero"
#print(type(mi_Nombre))# this return type "str" 

texto_largo = """ este texto 
contiene muchos 
saltos de linea""" #the triple comilla can help us to make a lot jump line and dont use the \

#print(texto_largo)

#---------------condicionales-----------------
#if a < d: #the conditional if help us to evalue a condition , in this case the condition it if a is greater than b 
#    print("el numero a es mayor")
#else: # tambien el else nos muestra opcion falsa sea el caso por ejemplo , si a es menor que b , a no lo es entonces no entra en la primera opcion entonces va a la segunda
#    print("el numero b menor ")


#------------------Funciones------------------

#def Mostrar():
    #print("javier")
    #print("alejandro")
    #print("kuznik")

#Mostrar()

#---------Funciones con parametros--------

#def Suma(a,b):
#    print(a+b)

#Suma(1,2)

#def SegundaSuma(a,b):
#    return a*b

#print(SegundaSuma(2,6))


#--------- Listas ------

nuevaLista = [1,4,5,13,76]

#
#print(nuevaLista[1])# 4

nuevaLista[1]="maria" # cambio el 4 por maria

#print(nuevaLista[-1]) #este me da la de derecha a izquierda siendo -1 el ultimo : 76

#print(nuevaLista[0:3])#esto solo nos muestra una porcion de la lista en este caso de la primera hasta la tercera poscicion 

nuevaLista.append("leandro")#agrega un elemento al final de la lista 

nuevaLista.insert(2,87192)#agrega donde nosotros le decimos por ejemplo en el indice 2 

nuevaLista.extend(["marta",712.42,True,"faqu"])#aqui concatenamos esat "lista" con la que ya tenemos

#print(nuevaLista[:])

#print("maria" in nuevaLista)#esto nos comprueba si un objeto esta en la lista o no , y nos devuelve true o false

nuevaLista.remove("marta")#remueve el elemento que le indicamos 

nuevaLista.pop()#remueve el ultimo elemento de la lista

nuevaLista2 = nuevaLista + ["maria","faqu",241,False]

print(nuevaLista2[:])