
#aqui guardaremos unos comandos para obtener iformacion de comentarios almacenados en funciones,metodos,clases...
#ej:

class Area:
    """
    La Clase Area alberga varias funciones para calcular areas de figuras geometicas
    """
    def AreaDeUnCuadrado(lado):
        #entonces imaginemos qeu queremos dejar un cometario o documento de lo qeu hace esta funcion
        """
        La funcion AreaDeUnCuadrado realiza respectivamente el calculo para obtener el are de un cuadrado
        """
        return "El area de un cuadrado es " + str(lado*lado)
    
    def AreaDeUnTriangulo(base,altura):
        """
        La funcion AreaDeUnCuadrado realiza respectivamente el calculo para obtener el are de un triangulo
        """
        return "El area de un triangulo es " + str((base*altura)/2)
    
"""
#teniendo nuestra clase y sus funciones, ahiora queremos obtener la documentacion qeu contienen 
#y eso lo logramos con :
help(Area)#esto nos dara toda la documentacion de la clase(con la de las funciones)

help(Area.AreaDeUnCuadrado)#tambien podemos consultar ayuda de una funcion en especifico 

help(Procedimientos)#tambien podemos consultar(siempre que importemos) la documentacion de 
#los modulos y las funciones que contienen"""


#------------------------------------------DocTest----------------------------------------

#con el doctest podemos probar las funciones antes de correlas
#imaginemos que tenemos una funcion suma 

def Sumar(n1,n2):
    """
    >>> Sumar(4,18)
    22

    >>> Sumar(21,72)
    93

    >>> Sumar(2,3)
    5

    #pero ahora cambiemoslo por otro valor
    #6 :esto nos tira un error diciendo que NOSOTROS esperamos un 6 poro obtuvimos un 5 
    
    #ahora imaginemos que el resultado es un string , bueno solo debemos poner lo que se espera que devuelva:
    #El resultado de la suma es 5
    # y esto justamente no delvovera nada ya que esta bien 
    #tambien podemos hacer varias pruebas:
    """
    return n1+n2

import doctest
doctest.testmod()
