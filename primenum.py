import sympy

i = 0
res = []

while i>=0:
    if sympy.isprime(i) == True:
        res.append(i)
    if len(res) == 20:
        break
    i += 1

print(res)

