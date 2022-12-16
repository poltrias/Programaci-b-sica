def sumaNumeros(n):
    if n==1:
        return 1
    else:
        return n+sumaNumeros(n-1)

print(sumaNumeros(4))