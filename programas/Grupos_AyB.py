"""PROGRAMA 6

Escribir un programa que pregunte al usuario su nombre y sexo, y que posteriormente
muestre en pantalla el grupo al que corresponde. Para esto se debe asignar a un grupo de
acuerdo al nombre y el sexo del alumno. El grupo A lo conforman las mujeres con un nombre
anterior a la “M” y los hombres cuyo nombre inicia posterior a la “N”. Mientras el grupo B esta
conformado por el resto de alumnos."""

print("¿A cuál grupo perteneces, A o B? \n")

name = input("¿Cuál es tu nombre? ").title()
genders = input("Aquí va tu sexo, sólo escribe: `H´ o `M´ ").upper()

if genders == "M" and name[0] < "M" or genders == "H" and name[0] > "N":
    print("Perteneces al grupo A.")
else:
    print("Perteneces al grupo B.")
#Recuerda Python sabe cual es el abecedario y para acceder a la inicial de mis nombres es como en una lista [0]