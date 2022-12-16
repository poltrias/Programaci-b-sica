def sumaNumeros(llista, n):
  suma = 0
  for numero in llista:
    suma += numero
  if suma==n:
      print("Els elements de la llista sumen", n)
  else:
      print("Els elements de la llista no sumen", n)

sumaNumeros([1,2,3], 4)

