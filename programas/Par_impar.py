"""PROGRAMA 4
Escribir un programa que pida al usuario un número entero
y muestre en pantalla si es par o impar."""

print("Números pares e impares. \n")
integers = int(input("Dame un número entero: "))

if integers%2 == 0:
    print("Tu número es PAR.")
else:
    print("tu número es impar.")