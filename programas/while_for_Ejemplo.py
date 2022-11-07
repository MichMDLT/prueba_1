suma_total = 0
inicio = eval(input("Inicio: "))
fin = eval(input("Fin: "))

while inicio != 0 and fin != 0:
    suma_parcial = 0
    for i in range (inicio, fin+1):
        suma_parcial = suma_parcial + i
    print(suma_parcial)
    suma_total = suma_total + suma_parcial
    inicio = eval(input("inicio: "))
    fin = eval(input("Fin: "))
print("La suma total es: ", suma_total)