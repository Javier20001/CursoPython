class Humano():
    def __init__(self, N , A , E , h):
        self.__nombre = N
        self.__altura = A
        self.__edad = E
        self.__herramienta = h
    
    def getNombre(self):
        return self.__nombre
   
    def Usar(self):
        print(self.__nombre + " esta usando una " + self.__herramienta.getNombre())

class Herramienta():
    def __init__(self , n):
        self.__nombre = n

    def getNombre(self):
        return self.__nombre

Pala = Herramienta("pala")
faqu = Humano("faqu",1.65,21,Pala)
faqu.Usar()