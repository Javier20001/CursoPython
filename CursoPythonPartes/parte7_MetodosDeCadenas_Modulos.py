#---------------Metodo de cadenas------------------
"""
text = input("enter any text : ")
age = input("enter any age : ")
print("this is the text you choise : ", text.upper())#convert all letter in mayuscula 
print("this is the text you choise : ",age.lower())#minuscula
print("this is the text you choise : ",age.capitalize())#the first letter in mayuscula
print("this is the text you choise : ",age.count("h"))#this method count how many time the letter appears in the text
print("this is the text you choise : ",age.find('a'))#this method return the index where appears the letter
print("this is the text you choise : ",age.isalnum())#return truo o false if the text has letters and numbers
print("this is the text you choise : ", age.isalpha())#return true if the string have chars
print("this is the age you choise : ", age.isdigit())#this tell us if the text is a number or not 

age = input("enter any age : ")
while(age.isdigit()):
    if(int(age)>18):
        print("you can pass")
        break
    else:
        print("you are very yough")
        break
"""
#-------------------------MODULOS------------------------------

from __future__ import division
from Calculoos.CalculosGenerales import *
#print(Redondear(Division(4,17)))

mensaje = "hola"

print(mensaje[0])

















