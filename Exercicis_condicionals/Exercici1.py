import random
randomlist = random.sample(range(1, 20), 10)
print(randomlist)
for i in randomlist:
    if i%2 == 0:
        print("El numero", i, "es par")
    else:
        print("El numero", i , "es impar")
