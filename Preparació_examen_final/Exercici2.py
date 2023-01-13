def treureVocals():
    paraula=input("Escriu una paraula: ")
    for lletra in paraula:
        if lletra=="a" or lletra=="e" or lletra=="i" or lletra=="o" or lletra=="u":
            lletra=""
        else:
            print(lletra, end="")

treureVocals()