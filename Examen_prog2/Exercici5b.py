def sumaDigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumaDigits(n//10)

print(sumaDigits(394))
