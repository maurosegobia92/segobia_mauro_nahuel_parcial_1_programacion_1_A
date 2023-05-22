#1. Crear una función llamada aplicarAumento que reciba como parámetro el 
#precio de un producto y devuelva el valor del producto con un aumento del 5%. 
#Realizar la llamada desde el main.

def aplicarAumento (float):
    precio = float
    aumento = (precio*5/100) + precio
    return aumento


aumento = aplicarAumento(100)

print(aumento)
