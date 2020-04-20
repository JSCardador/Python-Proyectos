num = int(input("Ingresa un numero"))

if (num >1):
    for i in range (2, num//2):
        if(num%i) == 0:
            print("{} no es un numero primo.".format(num))
            break
    else:
        print("{} es un numero primo.".format(num))

else:
    print("{} no es un numero primo.".format(num))