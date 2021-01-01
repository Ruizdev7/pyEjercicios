#BUCLES

#Bucle for determinado

#for variable in elemento a recorrer
#    cuerpo de bucle

'''
for i in [1,2,3]:
    print("Hola")

for i in ["Primavera","Verano","Otono","Invierno"]:
    print(i)
'''

#como recorrer cadenas de texto, uso del tipo range, notaciones especiales con print

'''
contador=0 #introduccion a el uso de contadores o acumuladores
email=False
miEmail=input("Ingrese un correo electronico porfavor:")

for i in miEmail:

    if(i == "@" or i == "."):
        
        contador=contador+1

if contador==2:
    print("El email ingresado es correcto") #, end="   ")   #Incluye funcion end que permite separar los elementos generados en este caso por medio de espacios
else:
    print("El email ingresado no es correcto")

for i in range(5):
    print("Hola")
    print(i)
    
'''

#usos de range

'''
for i in range(5):
    print(f"valor de la variable {i}")# une cadenas de texto con el valor de la variable i 

#diferentes notaciones de la funcion range

for i in range(15, 57, 2):
    print(f"valor de la variable {i}")# une cadenas de texto con el valor de la variable i 

#for i in range(5):
#    print(f"valor de la variable {i}")# une cadenas de texto con el valor de la variable i 

#for i in range(5):
#    print(f"valor de la variable {i}")# une cadenas de texto con el valor de la variable i 

'''

#ciclos While caso donde el bucle while es determinado

#i=1

#while i <= 10:
#    print("Ejecucion" + str(i))
#    i=i+1

#print("Termino la ejecucion")

'''
#ciclo While caso donde el bucle es indeterminado

edad=int(input("Introduce tu edad porfavor: "))

while edad < 0 and edad <50:
    print("Haz introducido una edad negativa, vuelve a intentarlo")
    edad=int(input("Introduce tu edad porfavor: "))

print("Gracias")
print("Edad del aspirante: " + str(edad))

'''

'''
import math
print("Programa para el calculo de la raiz cuadrada")
numero=int(input("Introduce un numero porfavor: "))

intentos=0

while numero < 0 :
    print("No se puede hallar la raiz de un numero negativo")

    if intentos == 2:
        print("Has consumido los intentos disponibles")
        break;
    
    numero=int(input("Introduce un numero porfavor: "))
    if numero < 0 :
        intentos = intentos + 1

if intentos < 2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero)+ " es "+ str(solucion))
'''

#Conociendo las instrucciones Continue, pass y else

for letra in "Python":

    if letra=="h":       #Evalua si la variable que recorre contendra el valor h
        continue         #No ignora la h solo salta el resto del contenido del bucle y retorna al inicio del cuerpo del for


    print("Viendo la letra: " + letra )


while True:
    pass

class miclase:
    pass

def funcion:
    pass














































