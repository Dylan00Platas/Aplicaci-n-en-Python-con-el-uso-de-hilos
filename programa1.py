import threading
import os

#Omar Dylan Segura Platas

def tarea1():
    print("Realizando Tarea 1 en el Hilo: {}".format(threading.current_thread().name))
    print("Identificación del hilo ejecutando la Tarea 1: {}".format(threading.current_thread().ident))
    
def tarea2():
    print("Realizando Tarea 2 en el Hilo: {}".format(threading.current_thread().name))
    print("Identificación del hilo ejecutando la Tarea 2: {}".format(threading.current_thread().ident))
  
if __name__ == "__main__":
    print("Identificación del proceso ejecutando el programa principal: {}".format(os.getpid()))
    print("Identificación del hilo principal ejecutando el programa principal: {}".format(threading.current_thread().ident))
    print("Nombre del Hilo Principal: {}".format(threading.current_thread().name))
    
hilo1 = threading.Thread(target=tarea1, name="Hilo 1")
hilo2 = threading.Thread(target=tarea2, name="Hilo 2")

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Finalización del código")
