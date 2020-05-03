def sortWords(myString):
    words = myString.split()
    words.sort()
    print("Ordenadas alfabeticamente: ")
    n=0
    for word in words:
        n+=1
        print(f"{n}. {word}")


sortWords("Esta frase se ordena alfabeticamente")