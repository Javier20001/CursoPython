"""
#----------------------Bucles-----------------
List = [11,22,39,46,54,61,73]
for i in List:
    print(i)

List = [11,22,39,46,54,61,73]
for i in List:
    print(i,end=" , ") #with end we can modify how showed the values in the terminal when they end 

for i in "kuznikjavier@gmail.com":#also we can use a string for a for 
    print(i)

def Validacion_de_correo(mail):
    email = False
    a = 0
    cum = ""
    for i in mail:
        if i == '@':
            email = True
        elif i == ".":
            a = a + 1
        elif a == 1:
            cum = cum + i
        

    if email and cum == "com":
        print("el correo es correcto")
    else:
        print("el correo es incorrecto")

Validacion_de_correo(input())


#---------------notaciones en el print------------

for i in range(5):#tambien podemos indicar el largo : 5 , 50 -> esto seria que empezaria desde 5 y temrina en 50 
    print(f"el valor de i es {i}") # la f dentro del print nos permite concatenar el str con los int 


def Validacion_de_correo(mail):
    email = False
    a = 0
    cum = ""
    for i in range(len(mail)):
        if mail[i] == '@':
            email = True
        elif mail[i] == ".":
            a = a + 1
        elif a == 1:
            cum = cum + mail[i]
        

    if email and cum == "com":
        print("el correo es correcto")
    else:
        print("el correo es incorrecto")

print("ingrese su mail: ")
Validacion_de_correo(input())



#------------------------bucle while --------------
import math


edad = False
while edad == False:
    age = int(input("ingrese sus edad pro favor "))
    if 7<age<70:
        print("puede pasar")
        edad = True
    else:
        print("edad incorrecta , ingresela otra vez ")


print("termino el rpograma")


import math

number = int(input("please enter a numer greater than 0: "))
opportunity = 0
while number <= 0:
    print("the number you choise is incorect, plase enter another one")
    number = int(input("please enter a numer greater than 0 again: "))
    opportunity = opportunity + 1
    if opportunity == 2:
        break


if opportunity != 2:
    result = math.sqrt(number)
    print(f"the solution is : {result}")
else:
    print("you enter to many time a incorect number,  plase try again later ")

""" 
#---------------continue , pass , else------------
text = "faqu es un chupa pija y lo queremos igual"
contador = 0
for i in text:
    if i == " ":
        continue#the continue keyword works to skip the code lines who are under this one(obviously only those that are inside the loop)
    contador = contador + 1

print("texto tiene una total de: " + str(contador) + " caracteres") 

#--------else in for ---------
mail = input("enter your mail address ")

for i in mail:
    if i == "@":
        arroba = True
        break
else:#first , this else belongs the for , if the for are complete(mean the "i" go through everything) so will go through the "else"
    arroba = False #while the for never ended 

print(arroba)
