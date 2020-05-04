

def ArmstrongInterval (n1, n2):
    ArmstrongNumbers = []
    for n in range(n1, n2+1):
        Sum =0
        tempN=n
        order = len(str(n))

        while tempN > 0:
            digit = tempN % 10
            Sum +=digit**order
            tempN //=10

        if n == Sum:
            ArmstrongNumbers.append(n)
            
    print(f"Los numeros narcisistas entre {n1} y {n2} son: \n {ArmstrongNumbers}")

ArmstrongInterval(100,2000)