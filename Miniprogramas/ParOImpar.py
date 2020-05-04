# Script que devuelve si el numero es par o impar.

###
# Logica: Si el modulo de 2 del numero proporcionado es cero
# el numero será par.
# En caso contrario sera impar.
# ###
def OddOrEven(number):
    if(number % 2 == 0):
        print(f"El numbero {number} es par")
    else:
        print(f"El numbero {number} es impar")

OddOrEven(23679)
