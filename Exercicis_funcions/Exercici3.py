def capicua():
    numero=(input("Introdueix un numero: "))
    numero_al_reves=numero[::-1]
    numero_al_reves=int(numero_al_reves)
    if numero==numero_al_reves:
        print("El numero", numero, "es capicua")
    else:
        print("El numero", numero, "no es capicua")

capicua()