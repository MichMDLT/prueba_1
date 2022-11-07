"""PROGRAMA 2
Escribir un programa que guarde la cadena “password” en una variable,
 y pregunte al usuario por la contraseña, realice una comparación entre
 la variable y la contraseña ingresada por el usuario e imprima por pantalla
 si la contraseña introducida por el usuario coincide con la guardada en la variable
 sin tener en cuenta mayúsculas y minúsculas"""
"""
contrasegna = "Password"
cont_entrada =input("Escribe aquí tu contraseña: ").title()

if cont_entrada == contrasegna:
    print("Contraseña correcta.")
else:
    print("No es correcto.")
"""
"""SeGUNDA parte:
Escribir un programa que pida al usuario una contraseña, 
que la almacene en una variable y una vez guardada, 
pregunte al usuario cual es la contraseña, si la contraseña 
es correcta, mostrar un mensaje que indique " Contraseña correcta", 
de lo contrario pedir la contraseña 5 veces, 
despues de esos 5 intentos salir del programa."""


contrasena = input("Escribe tu contraseña: ")
pass_ingresado = input("Escribe la contraseña del sistema: ")
for i in range(5):
    if pass_ingresado != contrasena:
        print("Contraseña incorrecta.")
        pass_ingresado = input("Escriba nuevamente la contraseña del sistema: ")
    else:
        print("La contraseña es correcta.")
        break
