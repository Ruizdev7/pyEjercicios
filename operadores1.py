# Uso de algunos operadores en Python 

edad = -7

if 0 < edad < 100:   #Concatenacion de operadores se leen de derecha a izquierda
    print("La edad es correcta")
else:
    print("La edad es incorrecta")

#La funcion str permite concatenar el valor entre parentesis con una cadena de texto no se puede cadena y numero

salario_presidente=int(input("Introduce el salario del presidente : "))
print("El salario del presidente es: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("El salario del director es: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area: "))
print("El salario del jefe de area es: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("El salario del administrativo es: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona bien")
else:
    print("Algo anda mal")


# Operadores logicos
print("Programa de becas año 2021")
distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
numero_hermanos=int(input("Introduce el numero de hermanos con los que cuenta el alumno: "))
salario_familiar=int(input("Introduce el salario anual familiar en pesos: "))

print(distancia_escuela)
print(numero_hermanos)
print(salario_familiar)


if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar<=20000:
    print("Tiene derecho a beca")

else:
    print("No tienes derecho a beca")


minuscula="esto es una cadena en minuscula"
MAYUSCULA="ESTO ES UNA CADENA EN MAYUSCULA"

MINUSCULA=minuscula.upper()
mayuscula=MAYUSCULA.lower()

print(MINUSCULA)
print(mayuscula)

















