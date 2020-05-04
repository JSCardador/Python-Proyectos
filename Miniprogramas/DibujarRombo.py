# Scripts para dibujar por consola un Rombo con asteriscos
# n = Numero de lineas del Rombo

def Rombo(n):
    for i in range(1, n + 1):
        print(" " *(n-i) + "* " * i)
    for j in range(1, n):
        print(" " * j + "* " * (n-j))


Rombo(7)
