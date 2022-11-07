i = 1
suma = 0
print("Introduce una serie de numeros. Si es 0 habrás terminado la lista")
print("Numero", i, ":", end="")
numero = eval(input())
print(numero)
suma = suma+numero
while numero != 0:
    i = i + 1
    print("Numero", i, ":", end="")
    numero = eval(input())
    print(numero)
    suma = suma + numero

print("La suma de todos los numeros es:", suma)