llista_productes={"platan":4.20,"enciam":0.69,"dildo":69,"caramel":2.34}
for producto, precio in llista_productes.items():
    print("Producto=", producto, ", Precio=", precio , "€")
    if precio<1:
        print("El producte es barat")
    elif precio>3:
        print("El producte es car")
    else:
        print("El producte no es ni car ni barat")
