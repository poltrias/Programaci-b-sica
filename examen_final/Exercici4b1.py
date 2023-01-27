def sumarParellsSenars(l):
    suma_parells = 0
    suma_senars = 0
    for numero in l:
        if numero % 2 == 0:
            suma_parells += numero
        else:
            suma_senars += numero
    print(suma_parells, suma_senars)


sumarParellsSenars([2, 3, 4, 6, 7])
sumarParellsSenars([-2, 5, 6, -3, 2, 14, 12, 9, 13])
#ESTA MALAMENT HE SUMAT ELS PARELLS I SENARS M'HE FUMAT LU DE LA POSICIÓ PERO EM FA PAL SEGUIR AMB AQUEST