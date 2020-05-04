# Script que indica si el año introducido es bisiesto

###
# Condiciones para un año sea Bisiesto:
#   1. Si un año es divisible entre 4, será bisiesto.
#   2. Si un año es divisible entre 4 pero no entre 100, es bisiesto.
#   3. Si un año es divisible entre 100 y entre 400, es bisieto.
# ###

def LeapYear(year):
    if(year % 4) ==0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                print(f"{year} fue un año bisiesto")
            else:
                print(f"{year} no fue un año bisiesto")
        else:
            print(f"{year} fue un año bisiesto")
    else:
        print(f"{year} no fue un año bisiesto")

LeapYear(1996)

