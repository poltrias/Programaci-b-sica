import random

numero_random=random.randrange(10)


numero2=int(input("Escull un numero per comparar: "))
numero2=int(numero2)

while numero_random != numero2:
    print("Los numeros no coinciden")
    numero2 = int(input("Escull un numero per comparar: "))
    if numero_random==numero2:
        print("Explota la bomba")
    else:
        pass


