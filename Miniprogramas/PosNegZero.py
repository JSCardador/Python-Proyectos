# Script que indica si el numero proporcionado es negativo, positivo o cero.

def PosNegZero(number):
    if(number>0):
        print(f"El numero {number} es positivo.")
    elif (number<0):
        print(f"El numero {number} es negativo.")
    elif (number==0):
        print(f"El numero {number} es cero.")
        
PosNegZero(-12)