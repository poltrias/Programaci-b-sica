l=[1,2,3,4,5,6,7]
suma_parells=0
suma_senars=0
for numero in l:
    if numero%2==0:
        suma_parells+=numero
    else:
        suma_senars+=numero

print("La suma dels nombres parells és de",suma_parells)
print("La suma dels nombres senars és de",suma_senars)
#ESTA MALAMENT