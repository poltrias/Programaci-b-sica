l=[1,222,12,45,86,243,7568,323]
def ParImpar():
    for numero in l:
        if numero%2==0:
            print(numero, "Es un numero par")
        else:
            print(numero, "Es un numero impar")

ParImpar()