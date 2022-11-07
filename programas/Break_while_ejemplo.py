suma = 0
print("El programa ira pidiendo números y los ira sumando hasta que la suma sea mayor a 100)")
while True:
    numero = eval(input("Introduce un número: "))
    suma = suma + numero
    if suma > 100:
        break
print("La suma total ha sido: ", suma)

#si pongo == 100 , debo tener exctamente loa números que me den 100
"""Si lo dejo el if como == 100
se le puede poner un controlador:
if suma == 100:
    break
i= i+1
print("la sum total: ", suma)   
 """
