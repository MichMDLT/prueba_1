import random

#págna 135
#El "format" es para hacerlo columna

print("El programa generara 20 datos aleatorios, divididos en 5 columnas")
print("En la columna 1: Enteros aleatorios de 0 a 10, ambos inclusive")
print("En la columna 2: Enteros PARES de 0 a 100 ambos inclusive")
print("En la columna 3: Reales aleatorios de 0.0 a 1.0, excluido este último")
print("En la columna 4: Reales aleatorios de 12.34 a 87.9832, sin seguridad este último")
print("En la columna 5: Elementos individuales de la cadena \"Nombre: Juan Edad: 27\"\n")

for i in range(0,20):
    numero_randint = random.randint(0,10)
    numero_randrange = random.randrange(0,100,2)
    numero_random = random.random()
    numero_uniform = random.uniform(12.34,87.9832)
    numero_choice = random.choice,"Nombre: Juan Edad: 27")

    print(format(numero_randint, "<2"),end=" ")
    print(format)