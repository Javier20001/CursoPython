#---------------LAMBDA----------------

#las funciones lambda sirven para reducir el codigo en una funcion sin mucha logica,
#imaginemos que quermeos obtener la suma de dos numero , con una funsion comun lo hariamos asi 
"""def Sumar(numero1, numero2):
    return (numero1 + numero2)"""

#llamamos a la funsion y ya , bueno ahora vamos hacer lo mismo con las funciones lambda

FuncionSuma = lambda numero1,numero2: numero1+numero2 
#inciamos poniendo el nombre de la funcion igualado a la palabra clave "lambda"
#y a continuacion los parametros , ponemos dos puntos y lo que necesitamos que devuelva o haga 
# -------------AVISO--------------
# NO SE PUEDE USAR BUCLES O DEMASIADAS LINEAS EN UNA FUNCION LAMBDA , DEBEN SER FUNCIONES MUY SIMPLES 

#y se llama de la siguiente forma:

#print(FuncionSuma(2,3))

#otro ejemplo:
"""
FuncionElebar = lambda numero , exponente: pow(numero,exponente)
print(FuncionElebar(3,4))"""


#------------FILTER--------
#en resumen el filter ayuda aplicar una condicon a objetos de una lista o array iterable , por ejemplo , tenemos una lista de numero 
#y queremos filtrar por pares , apliquemos ya que estamos lambda

"""ListaNumeros = (24,17,13,82,1028,9)
print(list(filter(lambda NumerosPares: NumerosPares % 2==0, ListaNumeros)))"""
#primero combirtamos el filter en una lista , ya que retornara varios numeros 
#y segundo , al filter hay qeu pasarle la funcion que ayudara a filtrar y una lista de datos 

#ahora hagamos lo mismo pero con objetos :

class Empleado:
    def __init__(self , nombre , cargo , salario):
            self.nombre = nombre
            self.cargo = cargo
            self.salario = salario

    def __str__(self) :
        return "{} trabaja como {} y tiene un salario de ${}".format(self.nombre,self.cargo,self.salario)


TuplaEmpleados = [
    Empleado("juan","Mercader",2343),
    Empleado("calos","Herrero",1343),
    Empleado("seba","Pescader",343),
    Empleado("Mordok","Guardia",7343)
]

##ListaAltoSueldo = filter(lambda empleado : empleado.salario > 500 , TuplaEmpleados)
#entonces creamos un filter que tiene la condicion de si el salio de un empleado es mayor a 500 , le pasamos la lista de empleados
# y guardamos el resultado en otra 

"""for i in ListaAltoSueldo:
    print(i)
"""

#----------------------MAP-----------------------
#la funcion map es similar al filter , solo que en vez de aplicar una condicion a un objeto de lista 
#le aplica una funcion 

#vamos usar la clase empleado de antes y funsion para calcularle una comision 

def CalcularComision(empleado):
    empleado.salario = empleado.salario * 1.03
    return empleado

ListaConComision = map(CalcularComision , TuplaEmpleados)

for i in ListaConComision:
    print(i)