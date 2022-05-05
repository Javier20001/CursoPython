#------------Tuplas--------------
#nuevaTupla = (1,6,"mario",4.21)#creamos una tupla 
#nuevaLista =  list(nuevaTupla)#convertimos una tupla en lista 
#print(nuevaLista[3]) 
#hasta aqui logramos convertir una tupla en lista ahora haremos lo opuesto 

nuevaLista =[1,6,"mario",4.21] #creamos una lista
nuevaTupla = tuple(nuevaLista) #inicializamos una tupla y le damos el valor de la lista convertida en tupla
#print(nuevaTupla[3])

#also we can ask if a values are in the tuple  
#print(4.21 in nuevaTupla)#true 

#we can ask  how many time a element are repeat in the tuple
#print(nuevaTupla.count(6))#1

#can ask what is the range of the tuple whit:
#print(len(nuevaTupla))#4

tuplaFechayNombre=("javier",10,1,2001)#here created a tuple with a name , day , month and year 
nombre, dia, mes, ano  = tuplaFechayNombre #and here created four variables for the correspondig values in the tuple, in this order 
# the variables go to have the specific values : the nombre have "juan", dia have "10" , etc
#so there is the test 
#print(nombre)

#print(nuevaTupla[0:3])

#i do a for example , not ignore me to much :)
#for i in nuevaTupla:
#    print(i)









#------------------------Diccionario--------------------

diccionarioPaises={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}#los diccionarios estan compuestos por claves(que seria como un indice) ylas claves tienen valores
#entonces para mostrar un valor solo tenemos que llamar a su clave 
#print(diccionarioPaises["Francia"])#Paris

#si queremos agregar mas codas al diccionario :
diccionarioPaises["Italia"] = "Buenos Aires"#obviamente esto esta mal pero ahora lo correiguimos 
#print(diccionarioPaises)
#y para cambiar el valor de una clave 
diccionarioPaises["Italia"] = "Roma"
#print(diccionarioPaises)

#para eliminar:
#del diccionarioPaises["España"]
#print(diccionarioPaises)


#tambien podemos usar tuplas o listas como claves
#tupla1 = ("Italia" , "Argentina" , "Francia" , "España")
#nuevoDiccionario = {tupla1[0]:"Roma", tupla1[1]:"Buenos Aires", tupla1[2]:"Paris",tupla1[3]:"Madrid"}

#print(nuevoDiccionario["Francia"])


#tambien los diccionarios pueden tener tuplas como valores 
#diccionarioTuplas = {"Nombre":"Javier", "Edad": 21 , "Fecha de Nacimiento":"10 de enero , 2001" , "Notas":[8,9,5,1,7,4,5]}
#print(diccionarioTuplas["Notas"])#como notas contiene una tupla la muestra 

#tambien podemos tener diccionarios dentro de un diccionario 
diccionarioDoble =  {"Nombre":"Javier", "Edad": 21 , "Fecha de Nacimiento":"10 de enero , 2001" , "Notas":{"Finales":[8,9,5,1,7,4,5]}}
#print(diccionarioDoble["Notas"])

#despues podemos solo obtener las claves(keys)
print(diccionarioDoble.keys())
#para mostrar solo lso valores hacemos
print(diccionarioDoble.values())
#y para saber el largo hacemos
print(len(diccionarioDoble))