#---------------Expresiones Regulares------------------

import re 

"""Cadena = "Hola vamos aprender sobre expresiones regulares en python , siendo python uno de los lenguajes mas practicos "
PalabraBuscar = "python"

#PalabraEncontrada = re.search(PalabraBuscar , Cadena)
if PalabraBuscar is not None :# el search nos permite buscar una palabra dentro de la cadena 
    #print("Palabra encontrada ")
    #print(PalabraEncontrada.start())#nos muestra donde empieza en la cadena la palabra que buscamos 
    #print(PalabraEncontrada.end())#nos muestra donde termina en la cadena la palabra que buscamos 
    #print(PalabraEncontrada.span())#nos muestra donde termina y acaba en la cadena la palabra que buscamos
    print(re.findall(PalabraBuscar,Cadena))#findall trae todas la veces que se repita esa palabra

else:
    print("no se encontro ni madres pa ")"""

ListaNombres = ['Ana Gomez',
                'Matias Martinez',
                'Sandra Lopez',
                'Santiago Martinez',
                'Sandra Fernandez'
]

ListaObjetos = ['Hombres',
                'Mujeres',
                'Mascotas',
                'niños',
                'niñas',]

"""for elemento in ListaNombres:
    if re.findall("^sandra",elemento):#colocando el ^ al lado de la palbra al buscar , le indicamos qeu busque en cada primera palabra de los nombres
        print(elemento)#esto debolvera "Sandra" de posicion 2 y de la 4

    if re.findall("Martinez$",elemento):# y colocar el $ busca concidencias en la palabra final  
        print(elemento)#debolveria la poscion 1 y 3 


for elemento in ListaObjetos:
    if re.findall("[ñ]",elemento):#si usamos corchetes y adentro las letras clave a buscar , nos retornara las palabras que tengan esa letras 
        print(elemento)

    if re.findall("[ñhj]",elemento):#tambien podemos con los corchetes meter varia letras claves y nos delvolveran las palabras que las contengan 
        print(elemento)

    if re.findall("niñ[oa]s",elemento):# tambien usar una plabra clave y que tenga adentro corchetes con letras claves 
        print(elemento)
    """

#----Rangos

ListaPersonas = ['Ana',
                'Marcos',
                'Nilda',
                'Cesar',
                'faqu',]

ListaID = ['AR0',
            'AR1',
            'VEN1',
            'AR2',
            'VEN2',
            'VEN3',
            'ARa',
            'ARb',
            'AR.',
            'AR:',]
"""
for elemento in ListaID:
    if re.findall("[Bb-d]",elemento):#lo que hacemos ahora en colocar un rango clave alfabetico con las letras b y d 
        print(elemento)#entronces ento mostrara las palbras que contengan estas letras claves osea: Marcos y Nilda
        #lo que si no delvovlera Cesar(ya que contiene una c) ya que es una C(mayuscula) y no c(minuscula) , asi que hay qeu aclararlo
    
    if re.findall("AR[0-1a-b.:]", elemento):#tambien funciona con numeros
        print(elemento)
    if re.findall("AR[^0-1]", elemento):#poniendo el ^ antes del rango le dimos que NO nos traiga eso 
        print(elemento)"""


#------Match----

nombre1 = "Lara Fernandez"
nombre2 = "Jara kuznik"
nombre3 = "Erik gonzales"
numero1 = "2712984712"
numero2 = "a2712984712"


"""for Nombre in ListaNombres:
    if re.match("Ana" , Nombre , re.IGNORECASE):#el IGNORECASE sirve para ignorar en caso de mayuscula y minuscula 
        print("nombre encontrado")

if re.match(".ara" , nombre1):#el . funciona como un comodin tomando cualquien letra y debolviendo el nombre que encaje con las otras 3 
    print("nombre encontrado")
else:
    print("nombre no encontrado")

if re.match("\d" , numero2):#el \d funciona para identificar numeros , no olvidemos que el match evalua siempre la primera letra , entonces so tiene una letra dejara de evaluar el resto de la cadena
    print("numero encontrado")#con numero1 todo esatra bien , con numero2 dira que no lo encontro 
else:
    print("numero no encontrado")"""


#-----Search----
#el search evalua toda la cadena , por eso buscaremos spor sus apellidos
if re.search('fernandez' , nombre1 , re.IGNORECASE):#si buscamos por su apellido con el search seguro lo encuentra
    print("nombre encontrado")#enontces lo encontro 
else:
    print("no lo encontre")

#tambien funciona con cadenas muuuuuuuuy largas 
ListaCodigos = ["gajfhgajhsgsgfhjahgjshagfjgasjgjhsgjfgajh71gajhsdfsagsags",
                "gfhjasgfjhasgfjhasgjh213jkhdjkashjkd",]

for i in ListaCodigos:
    if re.search('71',i):#le diremos que evalue la lista para saber si alguno de los codigos tiene el 71
        print(f"lo encontre: {i}")#y justamente uno si 