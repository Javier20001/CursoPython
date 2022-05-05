#--------------------Excepciones------------------
from os import system, name
from unittest import result

#this funtion help us to clear the terminal , please dont remuve 
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
"""
number = -1
while number < 0:
    try:#for first time we use the "Try" and the except , and whis this (works like a if else) cach an error and make a exceprion , while know the error 
        num = int(input("pro favor introduzca un numero y que sea mayor a 0 "))
        number = num
    except ValueError:
        print("you will enter a value not aceptable , please try again")
    clear()

def factorial(num):
    res = num
    while num != 1:
        if res == 0:
            res = 1
            break
        else:
            res = res * (num-1) 
            num = num
    return res 
# print(factorial(number))

#--------- own exception-------------
def ageCategory(age):
    if age < 0:
        raise TypeError("no accept negativve age")#here we create our own error,only if we provoke, the line code after this, will never be executed
    elif age<20:
        print("you are to young")
    elif age<40:
        print("you're still young, but not much")
    elif age<60:
        print("you're a men")

age = int(input("ingrese su edad "))
try: #although we can meke a exception to executed the rest of the code 
    ageCategory(age)
except TypeError as errorAgeNegative:#and here call de error name in the raise an rename like "errorAgeNegative" for indicate what is the problem 
    print("error de edad negativa")
"""

#--------------------------------OBJETOS EN PYTHON-------------------

