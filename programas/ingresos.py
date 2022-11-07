"""PROGRAMA 5
Escribir un programa que pregunte al usuario su edad y sus
ingresos mensuales, en caso de que el usuario sea mayor de edad
y sus ingresos mensuales sean mayores a $10,000.00 muestre en
pantalla que el usuario debe pagar impuestos."""

age = int(input("Dime tu edad: "))
ingr = float(input("A cuánto ascienden tus ingresos mensualmente: $ "))

if age >= 18 and ingr > 10000:
        print("Debes pagar impuestos.")
else:
    print("No debes pagar nada.")
