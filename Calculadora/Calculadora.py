import tkinter as tk
import math 

# Metodos

def clear():
   global operator 
   operator = ""
   numInputText.set("0")

def press_button(digit):
   global operator
   operator += str(digit)
   numInputText.set(operator)

def result():
   global operator
   try:
      r = str(eval(operator))
   except:
      numInputText.set("ERROR")
      return
   
   numInputText.set(r)
   operator = r

def Sqrt():
   global operator
   try:
      r = math.sqrt(int(operator))
   except:
      numInputText.set("ERROR")
      return

   numInputText.set(int(r))
   operator = str(int(r))

def Logarithm():
   global operator
   try:
      r = math.log2(int(operator))
   except:
      numInputText.set("ERROR")
      return
   
   numInputText.set(int(r))
   operator = str(int(r))

def Exp():
   global operator
   try:
      r = math.exp(int(operator))
   except:
      numInputText.set("ERROR")
      return
   numInputText.set(int(r))
   operator = str(int(r))



# Creación y configuracion del root de Tkinter
root = tk.Tk()
root.resizable(0,0)
root.title("JSC - Calculadora cientifica")
root.iconbitmap('Logo.ico')
rootFrame = tk.Frame(root)
rootFrame.config(relief = "sunken", bd = 10, bg = "lightgray", cursor = "dotbox")
rootFrame.pack(ipadx=5, ipady=5, fill = "x")


# Entrada de numeros superior
operator = ""
numInputText = tk.StringVar()

entryNumInput = tk.Entry(rootFrame, textvariable=numInputText, width =22, borderwidth = 10, font = ("Consolas", 20, "bold"),bg = "PaleTurquoise2")
entryNumInput.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 20)



# Botones numericos inputs
colorNumButton = "gray71"
widthButton = 10
heightButton = 5

buttonsFrame = tk.Frame(root, relief = "sunken", bg = "gray80", bd = 10)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "1", command= lambda: press_button(1)).grid(row = 0, column = 0, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "2", command= lambda: press_button(2)).grid(row = 0, column = 1, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "3", command= lambda: press_button(3)).grid(row = 0, column = 2, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "4", command= lambda: press_button(4)).grid(row = 1, column = 0, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "5", command= lambda: press_button(5)).grid(row = 1, column = 1, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "6", command= lambda: press_button(6)).grid(row = 1, column = 2, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "7", command= lambda: press_button(7)).grid(row = 2, column = 0, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "8", command= lambda: press_button(8)).grid(row = 2, column = 1, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "9", command= lambda: press_button(9)).grid(row = 2, column = 2, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "0", command= lambda: press_button(0)).grid(row = 3, column = 0, padx=5, pady = 5)

tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = ".", command= lambda: press_button(".")).grid(row = 3, column = 1, padx=5, pady = 5)
tk.Button(buttonsFrame, bg = colorNumButton, width = widthButton, height = heightButton, text = "Pi", command= lambda: press_button("pi")).grid(row = 3, column = 2, padx=5, pady = 5)



# Botones de operadores
colorOpeButton = "gray60"

tk.Button(buttonsFrame, text = "/", bg = colorOpeButton, width = widthButton, height = heightButton, command= lambda: press_button("/")).grid(row = 0, column = 3, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "x", bg = colorOpeButton,width = widthButton, height = heightButton, command= lambda: press_button("*")).grid(row = 1, column = 3, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "-", bg = colorOpeButton, width = widthButton, height = heightButton, command= lambda: press_button("-")).grid(row = 2, column = 3, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "+", bg = colorOpeButton, width = widthButton, height = heightButton, command= lambda: press_button("+")).grid(row = 3, column = 3, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "Raiz", bg = colorOpeButton, width = widthButton, height = heightButton, command= Sqrt).grid(row = 4, column = 0, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "C", bg = colorOpeButton, width = widthButton, height = heightButton, command= clear).grid(row = 4, column = 1, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "Exp", bg = colorOpeButton, width = widthButton, height = heightButton, command= Exp).grid(row = 4, column = 3, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "=", bg = colorOpeButton, width = widthButton, height = heightButton, command= result).grid(row = 4, column = 2, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "(", bg = colorOpeButton, width = widthButton, height = heightButton, command= lambda: press_button("(")).grid(row = 5, column = 0, padx=5, pady = 5)
tk.Button(buttonsFrame, text = ")", bg = colorOpeButton, width = widthButton, height = heightButton, command= lambda: press_button(")")).grid(row = 5, column = 1, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "%", bg = colorOpeButton, width = widthButton, height = heightButton, command= lambda: press_button("%")).grid(row = 5, column = 2, padx=5, pady = 5)
tk.Button(buttonsFrame, text = "Ln", bg = colorOpeButton, width = widthButton, height = heightButton, command= Logarithm).grid(row = 5, column = 3, padx=5, pady = 5)

buttonsFrame.pack(anchor="center", fill="y")



# Loop del root
root.mainloop()
