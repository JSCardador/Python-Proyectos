def SumNatNumbers(Number):
    TempNumber = Number
    if Number < 0:
        print ("Inserta un numero positivo.")
    else:
        Sum =0 
        while(TempNumber > 0):
            Sum += TempNumber
            TempNumber-=1

        print(f"El sumatorio de {Number} es {Sum}")

SumNatNumbers(160)