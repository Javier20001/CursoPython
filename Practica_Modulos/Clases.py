class Persona():
    def __init__(self,n,a,s) :
        self.__name = n 
        self.__age = a 
        self.__size = s
    
    def talk(self):
        print("hi , my name is " ,self.__name, " and i have " ,self.__age, "age old")

    def walk(self):
        print("im walking")

class Programador(Persona):
    def __init__(self,s,w,n,a,sz):
        super().__init__(n,a,sz)
        self.__salary = s 
        self.__workSector = w
    
    def talk(self):
        super().talk()
        print("i programing things")
    
    def workerDescription(self):
        print("i work as a " ,self.__workSector, "and pay me " ,self.__salary, " for month")

class Medico(Persona):
    def __init__(self,s,w, n, a, sw):
        super().__init__(n, a, sw)
        self.__salary = s 
        self.__workSector = w

    def talk(self):
        super().talk()
        print("i will save our live")

    def workerDescription(self):
        print("i work as a " ,self.__workSector, "and pay me " ,self.__salary, " for month")

class Chofer(Persona):
    def __init__(self ,s, w, n, a, sw):
        super().__init__(n, a, sw)
        self.__salary = s 
        self.__workSector = w

    def talk(self):
        super().talk(),print("i can take you anywhere")

    def workerDescription(self):
        print("i work as a " ,self.__workSector, "and pay me " ,self.__salary, " for month")
 