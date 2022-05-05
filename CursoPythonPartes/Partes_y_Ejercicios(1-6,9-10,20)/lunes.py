"""
import threading
def worke():
    #funcion que realiza el trabajo en el thread
    print ('Estoy trabajando para Genbeta Dev')
    return

threads = list()
for i in range(3):
    t = threading.Thread(target=worke)
    threads.append(t)
    t.start()


from time import sleep
import random
import threading
import logging

#logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] (%(threadName)-s) %(masage)s')

treads = []
waiting = []
#proceso a ejecutar
def processes(id):
    for i in range(10):
        print("hilo "+ str(id) + ": proceso ", str(i)+ "\n" , end='SALTO')
        sleep(random.random())
        waiting[id]=True
        while waiting[id]:
            pass

#crear hilos
for i in range(10):
    waiting.append(False)
    treads.append(threading.Thread(target=processes, args=(i,)))

#iniciar hilos
for i in range(10):
    treads[i].start()

#sincronizar hilos

while True:
    #verificar si todos los hilos han terminado un proceso 
    processedAll = True
    for i in range(10):
        if not waiting[i]:
            processedAll = False
            break
    
    #si todos terminaron un proceso continuar con el siguiente 
    if processedAll:
        for i in range(10):
            waiting[i]=False
    
    #si ya se acabaron todos los procesos 
    if not treads[0].is_alive():
        break
"""

import threading
import time

def useless_function(seconds):
    print(f'Waiting for {seconds} second(s)', end = "\n")
    time.sleep(seconds)
    print(f'Done Waiting {seconds}  second(s)')

t = threading.Thread(target=useless_function, args=[1])
start = time.perf_counter()

t.start()
print(f'Active Threads: {threading.active_count()}')
t.join()
end = time.perf_counter()
print(f'Finished in {round(end-start, 2)} second(s)') 