import math

def RaizCuadrada(ListaNumero):
    """
    La funcion devuelve una lista de la raiz cuadrada de numero dentro de la lista 

    >>> ListaDeNumero = []
    >>> for i in [4,9,16]:
    ...  ListaDeNumeros.append(i)
    >>> RaizCuadrada(ListaDeNumero)
    [2.0 , 3.0 , 4.0]
    """

    return [math.sqrt(n) for n  in ListaNumero]

import doctest
doctest.testmod()