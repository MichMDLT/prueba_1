"""
A ver... la serie de Fibonaccí inicia en 0
donde se suma 0 + 1 (que es el siguiente número después del cero) =2
Luego, a ese resultado, se le suma el anterior, 2+1 =3
Por lo que ese 3 debe ser sumado con el anterior, lo cual da 5.
De nueva cuenta a ese último número, se le suma su anterior: 3+5 =8
y así sucesivamente.
"""

print("Fibonacci\n")
start = 0
process = 1
finish = 0
while True:
    number = int(input('Dame otro número, pero esta vez que sea mayor a 1\n'
                       ' (que será el número de cifras Fibonacci impresas): '))
    if number > 1:
        break
print('1',end=", ")
#El end=', 'es para escribir el resultado en línea horizontal

for i in range(0,number):
    finish = start+process
    print(f'{finish}',end=", ")
#no me funciona el ,end=", "
    start = process
    process = finish
    print(" ")

#https://www.youtube.com/watch?v=sNjoLvV9nFI
