l = [3, 45, 656, 90, 23, 66]
def numerosCapicua(l):
    for numero in l:
        numero=str(numero)
        if numero==numero[::-1]:
            print("El numero", numero, "es capicua")
        else:
            pass
numerosCapicua(l)