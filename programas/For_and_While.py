# ESTRUCTURA: for i in range([INICIO,FIN,secuencia en que manejará valores])
#               print(bloque de instrucciones [if, print,dato,etc.])
# El número final siempre será -1

print('Ejemplo 1 FOR: ')

for i in range(1,11,2):
    print(i)

print('Ejemplo 2: ')

'''
De alguna forma i es para renglones y
 j para columnas
SINO especifico se ejecuta de 1 en 1.
'''

for i in range(7):
    print(i)

print('Ejemplo 3: ')

for i in range(3,7):
    print(i)

print('Ejemplo 4: ')

for i in range(3,12,3):
    print(i)

print('Ejemplo 5: ')

for i in range(12,3,-3):
    print(i)

print('Ejemplo 6: ')
# Se pueden poner decimales desde el bloque de insrtucciones
for i in range(1,9):
    print(i+.5)

print('Ejemplo 1 Comparación --> WHILE & FOR : ')
# ESTRUCTURA: while condición lógica de mantenimiento en bucle:
#               print(bloque de instrucciones [if, print,dato,etc.])
# Se detendrá hasta llegar a 0 = False

print('for i in range(7):')

i=0
while i <7:
    print(i)
    i = i +1

print('Ejemplo 2: ')
print('for i in range(3,7):')

i=3
while i <7:
    print(i)
    i= i+1

print('Ejemplo 3: ')
print('for i in range(3,12,3):')

i=3
while i <12:
    print(i)
    i=i+3

print('Ejemplo 4, DECRECIENTE: ')
print('for i in range(12,3,-3):')

i = 12
while i >3:
    print(i)
    i=i -3

print('Ejemplo 1 BREAK & CONTINUE: ')
for i in range(10):
    if i>7:
    break
    suma= suma + i
print('La suma con break ha sido: ', suma)
    suma = 0
    for i in range(10):
      suma = suma + i
    print('La suma sin break ha sido: ', suma)
