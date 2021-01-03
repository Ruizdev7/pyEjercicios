'''Como lanzar excepciones

Raise personaliza el mensaje que se le envia al usuario

def evaluaEdad(edad):
    if edad < 0:
        raise ZeroDivisionError("No se permiten edades negativas")
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres Joven"
    elif edad < 65:
        return "Eres Maduro"
    elif edad < 100:
        return "Cuidate"

print(evaluaEdad(-15))'''


#Funcion para el calculo de la raiz cuadrada de un numero entero positivo

import math

def calculaRaiz(num1):
    
    if num1 < 0 :

        raise ValueError ("El numero no puede ser negativo")

    else:

        return math.sqrt(num1)

op1=int(input("Introduce un numero por favor: "))

try:
    
    print(calculaRaiz(op1))

except ValueError as Errordenumeronegativo:

    print(Errordenumeronegativo)

print("Programa Terminado")


