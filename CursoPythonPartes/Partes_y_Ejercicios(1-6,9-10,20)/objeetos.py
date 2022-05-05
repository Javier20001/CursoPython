
class Humano():
    def __init__(self, N , A , E ):
        self.__nombre = N#firts , for encapsul variables or metodos we have to put before de name a "__" double guion dawn
        self.__altura = A
        self.__edad = E

    def Hablar(self):
        print("hola mi nombre es" , self.__nombre , "como estas")
        
    def Descripcion(self):
        print("tengo una altura de", self.__altura , ",y tengo", self.__edad ,"años")

    #condicionales para saber si se mueve o no 
    def Caminar(self,wake_up,lunch,have_Pants):
        self.__moverme = self.Estatus(wake_up,lunch,have_Pants)
        if self.__moverme:
            print("estoy caminando , y me estoy cansando ....")
        else:
            print("nunca desperte , jamas almorce o no traigo pantalones")
    
    def __Estatus(self,wake_up,lunch,have_Pants): #the same for the metodos 
        self.desperte = wake_up
        self.almorce = lunch
        self.TengoPantalones = have_Pants
        if (self.desperte and self.TengoPantalones) or (self.almorce and self.TengoPantalones):
            return True
        else:
            return False


#-------------------------------------HERENCIA--------------------

#usamos la clase que creamos anteriormente y la usamos como superclase(abuelo) , y ahora creamos una subclase(medico, padre) , que hereda todos los metodos 
#hablar , caminar , descripcion 
class Medico():
    def __init__(self,o,s,p):
        self.__ocupacion = o
        self.__sueldo = s
        self.__piso = p

    def ocupacion(self):
        print("soy un "+ self.__ocupacion +", te salvare la vida")

class cirujano(Medico,Humano):
    pass



medico1 = cirujano("cirujano",18.000,"segundo piso")
medico1.ocupacion()
medico1.Descripcion()