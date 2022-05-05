#-----Decoradores----------
#como su nombre indica , sirven para decorar (o agregar ) codigo a funciones ya hechas 



#aqui tenemos dos funciones que representan (ezquisofrenicamente) a 21 funciones 
#ahora imaginemos que queremos agregar algunos mensajes a las funciones de forma que solo necesitemos crear una 
#para eso creamos una funcion decoradora


def FuncionDecoradora(FuncionParametro):
    def FuncionInterior(*args, **kwargs):
        #acciones que decoran a las demas funciones
        print("se va a realizar un calculo:")

        FuncionParametro(*args,**kwargs)

        print("se resolvio el calculo.")

    return FuncionInterior

"""@FuncionDecoradora#y la llamamos con un @ antes de la funcion que quermos editar
def suma():
    print(f"10+21={10+21}")

@FuncionDecoradora
def resta():
    print(f"19-2={19-2}")"""


#ahora supongamos que le pasamos parametros a la funcion suma y resta 
@FuncionDecoradora
def suma(n1,n2):
    print(f"{n1}+{n2}={n1+n2}")

@FuncionDecoradora
def resta(n1,n2):
    print(f"{n1}-{n2}={n1-n2}")


#como ahora las funcioens usan parametros , el decorador tambien los necesita


suma(18,32)
resta(12,6)


#ahora imaginemos que tenemos una funsion que recibe por parametros valores "clave=valor"
@FuncionDecoradora
def Exponente(base, exponente):
    print(pow(base,exponente))

Exponente(base=5,exponente=6)#al pasarles argumentos de tipo "clave=valor" , y si llamamos antes al decorador
#debemos editar los parametros que tambien recibe este mismo 