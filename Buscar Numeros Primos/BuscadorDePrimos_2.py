
def isPrime(n):
    if(n<=1):
        return False
    if(n<=3):
        return True
    if(n%2==0 or n%3==0):
        return print("{} no es un numero primo.".format(n))
    
    i=5
    while(i*i <=n):
        if(n%i == 0 or n%(i+2)==0):
            return False
        i=i+6
    return print("{} es un numero primo.".format(n))


isPrime(1999)