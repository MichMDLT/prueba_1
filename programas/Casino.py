"""
PROGRAMA 7
Escribir un programa para una casino que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
 El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
 Si el cliente es menor de 15 años puede entrar gratis, si tiene entre 15 y 25 años debe pagar
$50.00 pesos y si es mayor de 25 años, $80.00.
"""
print("'Entrada a Casino según edad'\n")

edge = eval(input("¿Cuál es tu edad? "))

if edge <= 15:
    print('Entra gratis.')
else:
    if edge > 16:
        if edge <= 25:
            print('Usted debe pagar $50 pesos en taquilla.')
        else:
            if edge > 26:
                print('Usted debe pagar $80 para en taquilla.')
