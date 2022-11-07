"""
Escribir un programa que pida al usuario un numero
entero positivo y que muestre en pantalla todos los
numeros impares separados por comas hasta el numero
elegido por el usuario
"""

numero =int(input("Dame numero entero positivo: "))

while numero < 0:
        numero = int(input("El número que diste es negativo, intenta con otro. "))
if numero == 0:
    print("No existen números impares positivos antes de cero.")
else:
    print("los numeros impares son: ")

    for i in range(1, numero+1,2):
        print(i,end=", ")

for i in range(1, numero+1):
    if i % 2 == 1:
        print(i,end=", ")
        
#Esta última fue lo que se me ocurría

"""Código del profe:
"""