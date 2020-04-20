from tkinter import * 
import random
import string

# Metodos
def GenerarPass():
    s = ""
    Characters = list(string.ascii_lowercase)

    
    if (NumVar.get()):
        Characters.extend(list(string.digits))
    if (MayVar.get()):
        Characters.extend(list(string.ascii_uppercase))
    if (SpeVar.get()):
        Characters.extend(list(string.punctuation))
    try:
        for i in range(int(maxCharacterInt.get())):
            s += random.choice(Characters)
    except:
        passwordStr.set("ERROR")
        return

    passwordStr.set(s)



def limitSizeCharacter(*args):
    value = maxCharacterInt.get()
    if len(value) > 2: maxCharacterInt.set(value[:2])

#Configuración del root de la interfaz Tkinter
root = Tk()
root.resizable(0,0)
root.title("JSC - Generador de contraseñas")
root.iconbitmap('Logo.ico')
rootFrame = Frame(root)
rootFrame.config(relief = "sunken", bd = 10)
rootFrame.pack(ipadx=5, ipady=5, fill = "x")

# Password
passwordStr = StringVar()
passInput = Entry(rootFrame, textvariable=passwordStr, width =22, borderwidth = 10, font = ("Consolas", 20, "bold"),bg = "PaleTurquoise2")
passInput.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 20)

# Entry Max Character 
Label(rootFrame, text="Total de caracteres:", justify="left").grid(row=1, column=1)
maxCharacterInt = StringVar()
maxCharacterInt.trace("w", limitSizeCharacter)
maxCharacterEntry = Entry(rootFrame, textvariable = maxCharacterInt, width = 2,justify="right")
maxCharacterEntry.grid(row = 1, column = 1, sticky = "e")

# CheckBox
NumVar = BooleanVar()
MayVar = BooleanVar()
SpeVar = BooleanVar()
Checkbutton(rootFrame, text="Numeros", variable = NumVar, onvalue = True, offvalue = False).grid(row=2, column = 1, padx=5, pady = 5)
Checkbutton(rootFrame, text="Mayusculas", variable = MayVar, onvalue = True, offvalue = False).grid(row=3, column = 1, padx=5, pady = 5)
Checkbutton(rootFrame, text="Caracteres especiales", variable = SpeVar, onvalue = True, offvalue = False).grid(row=4, column = 1, padx=5, pady = 5)


# Activate button

Button(rootFrame, text="Generar", command = GenerarPass).grid(row=5, column=1, pady = 10)

root.mainloop()
