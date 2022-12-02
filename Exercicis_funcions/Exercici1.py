def factorial():
    numero=int(input("Introdueix un numero: "))
    factorial=1
    if numero!=0:
        for i in range(1, numero+1):
            factorial=factorial*i
    print(factorial)

factorial()
