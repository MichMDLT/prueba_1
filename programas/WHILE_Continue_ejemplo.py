"""Sumar usando while, sumar los
10 primeros números, excepto los
múltiplos de 4"""

suma = 0
i = 0
while i < 10:
    i = i + 1
    suma = suma + i
print("La suma del 1 al 10 es: ", suma)

suma = 0
i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        print("El número que queda fuera es: ", i)
        continue
    suma = suma + i
print("La suma del 1 al 10, excepto los múltiplos de 4 es: ", suma)
