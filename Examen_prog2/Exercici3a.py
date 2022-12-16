def lletraEnString(string, lletra):
    if lletra in (string):
        print("La lletra", lletra, "es troba en la paraula", string)
    else:
        print("La lletra", lletra, "no es troba en la paraula", string)

lletraEnString("mamadouk", "d")
lletraEnString("mamadouk", "g")