class Persona():
    def __init__(self,n,a,s) :
        self.__name = n 
        self.__age = a 
        self.__size = s
    
    def talk(self):
        print("hi , my name is " ,self.__name, " and i have " ,self.__age, "age old")

    def walk(self):
        print("im walking")
"""
class Empleado(Persona):
    def __init__(self,s,w,n,a,sz):
        super().__init__(n,a,sz)
        self.__salary = s 
        self.__workSector = w
    
    def talk(self):
        super().talk()
    
    def workerDescription(self):
        print("i work as a " ,self.__workSector, "and pay me " ,self.__salary, " for month")

class Medico(Persona):
    def __init__(self,s,w, n, a, sw):
        super().__init__(n, a, sw)
        self.__salary = s 
        self.__workSector = w

    def talk(self):
        super().talk()

    def workerDescription(self):
        print("i work as a " ,self.__workSector, "and pay me " ,self.__salary, " for month")


Lucho = Empleado(14.000,"programmer","Lucho",26,1.75)
faqu = Persona("faqu",23,1.68)

print(isinstance(Lucho,Persona))
print(isinstance(faqu,Empleado))#the isintance help us to know who class belongs

"""
#----------------------------Polimorfismo----------------

class Programer(Persona):
    def __init__(self):
        self.__salary = 200000
        self.__workSector = "programador"
    
    def talk(self):
        super().talk()
    
    def workerDescription(self):
        print("i work as a " ,self.__workSector, "and pay me " ,self.__salary, " for month")

class Medico(Persona):
    def __init__(self):
        self.__salary = 18000
        self.__workSector = "cirujano"

    def talk(self):
        super().talk()

    def workerDescription(self):
        print("i work as a " ,self.__workSector, "and pay me " ,self.__salary, " for month")

def callDescription(Persona):
    Persona.workerDescription()

eric = Medico()#for make polymorphismonly has to chance de class whit we made de object 
#eric = Programer()#like this 
callDescription(eric)#so if we leave eric like this, this function will call the description it has in doctor