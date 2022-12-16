def cuenta_digitos(num):
  if num < 10:
    return 1
  else:
    return 1 + cuenta_digitos(num // 10)

print(cuenta_digitos(3))