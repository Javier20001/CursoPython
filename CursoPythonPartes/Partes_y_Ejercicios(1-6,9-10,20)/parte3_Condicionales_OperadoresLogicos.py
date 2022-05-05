#---------------------Condicionales-------------------

#nota = 5 #inicializamos a variable in 5 for the funtion 

#def evaluacion(nota):# sen the variable 
#    resultado = "desaprobado"# creamos el resultado 
#    if nota>=5: # here is the conditional and ask , "nota" is high o equals to 5 
#        resultado = "aprobado"#and if the condition is true , change de variable resultado 
#    return resultado #and here return that variable 

#resultado = evaluacion(nota) #here give to resultado the values of the funtion 
#print(resultado)

# now go to change a little the funtion 

"""
notaDelAlumno = input("ingrese la nota del alumno:")#the imput give us the chace to send a value  through the terminal , although the values ever go be the str type 

def evaluacion(nota):
    resultado = "desaprobado"
    if nota>=5: 
        resultado = "aprobado"
    return resultado

resultado = evaluacion(int(notaDelAlumno))#so , the ay to fix this problemas is changing the type of the input to int 
print(resultado)

#-------------------------------ELIF------------------
print("verificacion de acceso")

PersonAge = input("enter your age please:")

def Validacion(age):
    if age >= 18:
        print("you can go")
    elif age <= 70:
        print("alright .. but you not are older to be here? ")
    else:
        print("you are to young so you cant go , sorry little baby MUAJAJJAAJJ")

Validacion(int(PersonAge))


#-------------Condicionales 2----------
#a little example:
age = int(input("enter your age : "))

if 0<age<100: #here we're evaluating tho condition , if age less than 0 and if age greater 100
    print("the age are okey")
else:
    print("something its not alright")

#------------------------------AND, OR ,IN -------------------

DistanceSchool = int(input("enter the distance between your home and your school: "))
YourBrothers = int(input("enter how many brothers you have: "))
Salary =  int(input("enter your parente's salary "))

def becas(distance , brothers , salary):
    if distance > 40 and brothers > 2 or salary <= 20000:
        print("your request for the beca was acepted")
    else:
        print("your request for the beca was denied ")

becas(DistanceSchool , YourBrothers , Salary)
"""
print("programa de materias")
ListMatters = ("programming" , "math" , "ing software" , "orientation objet" , "ipc")
choise = input("enter the Subjects you choised plase: ").lower()
def Subjects(choise):
    if choise in ListMatters:
        print("your choice has completed successfully")
    else:
        print("the matter is not in the list ")

Subjects(choise)