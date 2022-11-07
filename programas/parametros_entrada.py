#Las funciones sirven para reutilizar código. Hacer cosas previas que hemos hecho antes.
def calculo_de_dos_datos():

    numero_1 =eval(input("Introduce el primer número: "))
    numero_2 =eval(input("Introduce el segundo número: "))
    resultado = ((numero_1 - numero_2) ** 2) + 1
    print("\nEl primer numero introducido ha sido: ", numero_1)
    print("\nEl segundo numero introducido ha sido: ", numero_2)
    print("La diferencia entre ellos elevada al cuadrado y luego sumado 1 es: ", resultado)

def main():
    for i in range(0, 3):
        calculo_de_dos_datos()

main()

"""
main es para ejectutar el programa principal pag. 144
"""