estic_a_casa=True
while estic_a_casa is True:
    paja=input("Paja?: ")
    if paja=="si" or paja=="Si":
        satisfet=input("Estas satisfet?: ")
        if satisfet=="si" or satisfet=="Si":
            print("Me'n vaig a dormir")
            break
        elif satisfet=="no" or satisfet=="No":
            print("Vaig a fumar")
            break
        else:
           print("Resposta incorrecta")

    elif paja=="no" or paja=="No":
        jugo_lol=input("Jugo al lol?: ")
        if jugo_lol=="si" or jugo_lol=="Si":
            print("M'he enfadat")
            break
        elif jugo_lol=="no" or jugo_lol=="No":
            print("Doncs al final si que em fare una paja")
            break
        else:
            print("Resposta incorrecta")
    else:
        print("Resposta incorrecta")
