"""
Sumar todos los números de 1 al 100, excepro el 3,19 y 32
"""
suma = 0
for i in range(101):
    if i == 3 or i == 19 or i == 32:
        continue
    suma = suma + i
print("La suma sin tomar en cuenta el 3, 19 y 32, es: ", suma)

suma = 0
for i in range(101):
    suma = suma + i
print("La suma sin tomar en cuenta el 3, 19 y 32, es: ", suma)

"""
En la feria los juegos de botella con aro
Continue, es que va mal y ya ando aventando otro.
Break es que me doy por vencida y me voy de la feria :(.
"""