def maxim_comu_divisor(a, b):
    if b == 0:
        return a
    return maxim_comu_divisor(b, a % b)


def minimo_comun_multiplo(a, b):
    return (a * b) / maxim_comu_divisor(a, b)

a=6
b=20
mcm = minimo_comun_multiplo(a, b)
mcd = maxim_comu_divisor(a, b)
print(mcm)
print(mcd)
