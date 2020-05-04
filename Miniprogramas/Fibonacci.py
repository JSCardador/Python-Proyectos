# Script  para buscar los numeros de la sucesión de Fibonacci hasta el numero indicado

def fibonacci(number):
    n, n1, n2 = 0, 0, 1
    FibonacciListNumber = [0, 1]
    while n<number:
        n = n1+n2
        n1 = n2
        n2 = n
        if n <= number:
            FibonacciListNumber.append(n)

    print('La lista de numeros de Fibonacci es de {} y son los siguientes: '.format(len(FibonacciListNumber)), FibonacciListNumber)

fibonacci(1000)
    
