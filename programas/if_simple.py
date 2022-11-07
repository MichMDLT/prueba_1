"""PROGRAMA 1
#Escribir un programa que pregunte al usuario su edad y se muestre en pantalla si la persona es mayor de edad o no."""

edad =int(input("Dime tu edad: "))
pais = input("De qué país eres: ").upper()
if pais == "MEXICO":
    if edad >= 18:
     print("Es mayor de edad en México.")
     if edad < 21:
         print("Pero eres menor de edad en USA.")
    else:
        print("Eres menor de edad en México.")
#En en el  else no van condiciones.

elif pais == "USA":
    if edad >= 21:
        print("Eres mayor de edad en USA.")
    else:
        print("Eres menor de edad en USA.")
#la fn .upper() se puede aplicar a los IF de los países.
else:
    print("Eres de un país diferente.")

