import concurrent.futures

# Omar Dylan Segura Platas

def hilo1():
    print("Ejecutando Hilo 1")

    for i in range(0, 6):
        print(i)

def hilo2():
    print("Ejecutando Hilo 2")

    for i in range(6, 12):
        print(i)

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(hilo1)
pool.submit(hilo2)

pool.shutdown(wait=True)

print("Fin del hilo principal")
