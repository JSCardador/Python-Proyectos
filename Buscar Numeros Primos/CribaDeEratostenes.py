from time import time

def CribaDeEratostenes(n):
    PrimeNum = [num for num in range(2, n+1)]
    for num in PrimeNum:
        TempNum = num
        while TempNum <= n:
            TempNum += num
            if TempNum in PrimeNum:
                PrimeNum.remove(TempNum)


    print("Entre el 0 y el {} hay {} numeros primos y son: \n {}".format(n, len(PrimeNum), PrimeNum))

start_time = time()

# Introducir numero aqui
CribaDeEratostenes(1000000)

elapsed_time = time() - start_time
print("Tiempo de respuesta: %.10f seconds." % elapsed_time)