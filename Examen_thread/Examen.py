import threading
import time
from time import sleep
import random
import requests

urls = [
     'https://images.pexels.com/photos/305821/pexels-photo-305821.jpeg',
     'https://images.pexels.com/photos/509922/pexels-photo-509922.jpeg',
     'https://images.pexels.com/photos/325812/pexels-photo-325812.jpeg',
     'https://images.pexels.com/photos/1252814/pexels-photo-1252814.jpeg',
     'https://images.pexels.com/photos/1420709/pexels-photo-1420709.jpeg',
     'https://images.pexels.com/photos/963486/pexels-photo-963486.jpeg',
     'https://images.pexels.com/photos/1557183/pexels-photo-1557183.jpeg',
     'https://images.pexels.com/photos/3023211/pexels-photo-3023211.jpeg',
     'https://images.pexels.com/photos/1031641/pexels-photo-1031641.jpeg',
     'https://images.pexels.com/photos/439227/pexels-photo-439227.jpeg',
     'https://images.pexels.com/photos/696644/pexels-photo-696644.jpeg',
     'https://images.pexels.com/photos/911254/pexels-photo-911254.jpeg',
     'https://images.pexels.com/photos/1001990/pexels-photo-1001990.jpeg',
     'https://images.pexels.com/photos/3518623/pexels-photo-3518623.jpeg',
     'https://images.pexels.com/photos/916044/pexels-photo-916044.jpeg'
 ]

def download(url,id):
    img_data = requests.get(url).content#conseguimos el contenido de la url
    img_name = url.split('/')[4]#obtenemos un lista del url separada por el "/" y el 4 indica la posicion que deseamos
    img_name = f'{img_name}.jpg'
    print(f'downloading {img_name}')
    with open(img_name, 'wb') as img_file:
        img_file.write(img_data)
        sleep(random.random())
        print(f'downloading {img_name}')

start = time.perf_counter()
threads = [] #creamos una tupla para los hilos 
for i in urls:
    t = threading.Thread(target=download, args=[i,1282])#creamos un hilo
    t.start()#iniciamos el hilo
    threads.append(t)#i lo gregamos  a la tupla 
for thread in threads:
    thread.join()#impide que el programa termine hasta que los hilos lo hagan primero 
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')#simplemente para saber cuanto tardo 


"""lo que ocurre en este codigo es que usando hilos para lograr concurrencia , cada hilo 
de la tupla "threads" se encanrga de descargar un URL, entonces en vez de descargarlo llamando 
a la funcion por cada URL (sin usar hilos), el proceso tardaria mas. cuando se ejecutan 
los hilos el proceso alterna entre cada uno formado la concurrencia """