from os import system, name
from unittest import result
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

def Suma(n1,n2):
    return n1+n2

def Resta(n1,n2):
    return n1-n2

def Multiplicar(n1,n2):
    return n1*n2

def Division(divisor,dividendo):
    while divisor <= 0:
        try:
            divisor= int(input("pro favor introduzca un numero y que sea mayor a 0 ")) 
        except ValueError:
            print("you will enter a value not aceptable , please try again")
        clear()
    return dividendo/divisor

def Exponente(n1,exponente):
    return n1**exponente

def Redondear(n1):
    return round(n1)