import tkinter as tk
import random

options = ["Piedra", "Papel", "Tijeras"]
# Metodos

def Game():
    MachineChoice = random.choice(options)
    MachineChoiceText.set(MachineChoice)

    if MyChoice.get()==MachineChoice:
        r = "Empate"
    elif MyChoice.get() == options[0]:
        if MachineChoice == options[1]:
            r="Perdiste"
        elif MachineChoice == options[2]:
            r="¡Ganaste!"
    elif MyChoice.get() == options[1]:
        if MachineChoice == options[2]:
            r="Perdiste"
        elif MachineChoice == options[0]:
            r="¡Ganaste!"
    elif MyChoice.get() == options[2]:
        if MachineChoice == options[0]:
            r="Perdiste"
        elif MachineChoice == options[1]:
            r="¡Ganaste!"
    ResultText.set(r)

# Tkinter root and config
root = tk.Tk()
root.resizable(0,0)
root.title("JSC - Piedra, papel o tijeras")
root.iconbitmap('Logo.ico')
rootFrame = tk.Frame(root)
rootFrame.config(relief = "sunken", bd = 10)

# Your choice
MyChoice = tk.StringVar()
MyChoice.set(options[0])
dropdown = tk.OptionMenu(rootFrame, MyChoice, *options)
dropdown.grid(row= 1, column = 0, padx=5, pady = 5)

# Machine choice
MachineChoiceText = tk.StringVar()
MachineChoiceText.set("SUERTE!!")
machineLabel = tk.Label(rootFrame, textvariable = MachineChoiceText)
machineLabel.grid(row= 1, column = 2, padx=5, pady = 5)

tk.Button(rootFrame, text="Jugar!", command = Game).grid(row= 2, column = 1, padx=5, pady = 5)


# Result
ResultText = tk.StringVar()
ResultText.set("SUERTE!!")
ResultLabel = tk.Label(rootFrame, textvariable = ResultText)
ResultLabel.grid(row=3, column = 1, padx=5, pady = 7)

rootFrame.pack()
root.mainloop()