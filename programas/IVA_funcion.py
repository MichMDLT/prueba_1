"""
Escribir una función que calcule el total de una factura
 tras aplicarle el IVA. La función debe recibir la cantidad
 sin IVA y el porcentaje de IVA a aplicar, y devolver el total
  de la factura. Si se llama la función sin el parametro del porcentaje
   de IVA, deberá aplicar un 21%.
"""

def factura(cantidad, iva=21):
    cantidad_total = cantidad + cantidad*iva/100
    print("La cantidad a facturar con iva es: ", cantidad_total)

def compra():
    articulo1 = eval(input("Cuánto pagaste por el 1er art: "))
    articulo2 = eval(input("Cuánto pagaste por el 2do art: "))
    articulo3 = eval(input("Cuánto pagaste por el 3er art: "))
    suma = articulo1 + articulo2 + articulo3
    return suma

def main():
    cantidad = compra()
    iva = input("Escribe la cantiddad de iva a cobrar: ")
    if iva != "":
        factura(cantidad, eval(iva))
    else:
        factura(cantidad)

main()