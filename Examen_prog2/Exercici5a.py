def compteAscendent(n):
  if n == 0:
    return ""
  else:
    compteAscendent(n-1)
  print(n)

compteAscendent(8)