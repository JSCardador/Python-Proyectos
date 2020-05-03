def AreaTriangle(L1, L2, L3):
    # Calculo del semiperimetro
    s = (L1 + L2 + L3)/2
    # Calculo del area, basado en el semiperimetro
    area = (s*(s-L1)*(s-L2)*(s-L3))**0.5

    print("El area del triangulo es de {0:.2f}".format(area))

AreaTriangle(10, 7, 12)