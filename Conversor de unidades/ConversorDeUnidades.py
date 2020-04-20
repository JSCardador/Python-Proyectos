from tkinter import *
from math import log10

# Metodos
def ChangeOption(*args):
    Unit = var.get()
    if Unit == options[0]:
        labelUnitConvert.set(options[1])
    elif Unit == options[1]:
        labelUnitConvert.set(options[0])
    elif Unit == options[2]:
        labelUnitConvert.set(options[3])
    elif Unit == options[3]:
        labelUnitConvert.set(options[2])
    elif Unit == options[4]:
        labelUnitConvert.set(options[5])
    elif Unit == options[5]:
        labelUnitConvert.set(options[4])
    elif Unit == options[6]:
        labelUnitConvert.set(options[7])

    
def Convert(*args):
    try:
        n = int(value.get())
    except:
        outputValue.set("ERROR!")
        return
    Unit = var.get()

    if Unit == options[0]:
        r = n/1.609
    elif Unit == options[1]:
        r = n*1.609
    elif Unit == options[2]:
        r = n*2.205
    elif Unit == options[3]:
        r = n/2.205
    elif Unit == options[4]:
        r = (n*9/5) + 32
    elif Unit == options[5]:
        r = (n-32)*5/9
    elif Unit == options[6]:
        r = 10.*log10(1000*n)
    elif Unit == options[7]:
        r = 10**((n)/10.)
    

    outputValue.set(r)


# Tkinter root and config
root = Tk()
root.resizable(0,0)
root.title("JSC - Conversor de unidades")
root.iconbitmap('Logo.ico')
rootFrame = Frame(root)
rootFrame.config(relief = "sunken", bd = 10)

Label(root, text = "CONVERSOR DE UNIDADES", font = ("Consolas", 20, "bold")).pack(padx=5, pady = 5)

# Select unit
options = ["Kilometros", "Millas", "Kilogramos", "Libras", "Celsius", "Fahrenheit", "Vatios", "Decibelio"]
var = StringVar()
var.set(options[0])
dropdown = OptionMenu(rootFrame, var, *options, command = ChangeOption)
dropdown.grid(row= 0, column = 0, padx=5, pady = 5)

# Entry value
value = IntVar()
entry = Entry(rootFrame, textvariable=value)
entry.grid(row = 1, column = 0, padx=5, pady = 5)

# Unit to convert
labelUnitConvert = StringVar()
labelUnitConvert.set(options[1])
Label(rootFrame, textvariable = labelUnitConvert, justify = "right", anchor =  "e").grid(row = 0, column = 2, padx=5, pady = 5)

#Button to convert
Button(rootFrame,text = "Convertir", command = Convert).grid(row=0, column=1, padx=5, pady = 5)

# Output Value
outputValue = StringVar()
output = Entry(rootFrame, textvariable=outputValue)
output.grid(row = 1, column = 2, padx=5, pady = 5)


rootFrame.pack(ipadx=5, ipady=5, fill = "x")
root.mainloop()