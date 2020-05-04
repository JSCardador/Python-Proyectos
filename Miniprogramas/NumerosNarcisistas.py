# Script que indica si el numero proporcionado es un numero narcisista.
# Un numero narcisista es aquel que es igual a la suma de sus dígitos elevados a la potencia de su número de cifras

def ArmstrongNumber(n):
    Sum =0
    tempN=n
    order = len(str(n))
    
    while tempN > 0:
        digit = tempN % 10
        Sum +=digit**order
        tempN //=10

    if n == Sum:
        print(f"{n} es un numero narcisista.")
    else:
        print(f"{n} no es un numero narcisista.")

ArmstrongNumber(1634)