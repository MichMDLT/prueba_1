"""PROGRAMA 3

Escribir un programa que pida al usuario ingresar dos números,
el divisor y el dividendo y devuelva su división. Si el usuario
introduce cero en el divisor devolver un aviso de error."""

dividendo = int(input("Ingresa un número: "))
divisor = int(input("Ingresa otro número: "))

if divisor == 0:
    print("Esto es un error.")
else:
    print("El resultado es: " + str(dividendo/divisor))