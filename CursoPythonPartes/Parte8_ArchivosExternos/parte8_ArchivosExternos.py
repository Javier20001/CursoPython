from io import open

"""
#-----------------abrir y escribir-------------
nuevoTexto =  open("Archivo.txt","w")
textoAgregar = "tengo ganas de chupar un pito\nde preferencia negro"

nuevoTexto.write(textoAgregar)
nuevoTexto.close()


#----------------abrir y leer-------------------
nuevoTexto =  open("Archivo.txt","r")


segundoTexto = nuevoTexto.readlines()

nuevoTexto.close()

print(segundoTexto[1])

#-----------------abrir y agregar----------

nuevoTexto = open("Archivo.txt","a")

nuevoTexto.write("\ntambien uno asiatico")

nuevoTexto.close()
"""

nuevoTexto =  open("Archivo.txt","r")

print(nuevoTexto.read())


