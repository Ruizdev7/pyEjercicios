'''Generadores que son, funcionamiento, utilidades sintaxis

yield

Estructuras que extraen valores de una funcion y se almacenan en
objetos iterables (Listas, tuplas, Diccionarios)  podremos recorrerlos

Estos valores se almacenan de uno en uno 

Cada vez que un generador almacena un valor, esta permanece en un estado pausado
hasta que se solicita el siguiente, caracteristica conocida como suspension de estado

la funcion devuelve la lista entera de una vez, el generador genera un valor cada vez que sea llamada
diria que es importante el conocimiento de este aspecto ya que el hecho de que la aplicacion 
contenga estas funciones dinamicas podria ocupar menos recursos (improve performance)

def generaNumeros():
    yield numeros 
'''

#Ejercicio maquina que genera numeros pares


#def generaPares(limite):

#    num=1

#    milista=[]

#    while num < limite:

#        milista.append(num*2)
#        num = num + 1

#    return milista

#print(generaPares(10))


#def generaPares(limite):

#    num=1

#    while num < limite:

#        yield num * 2
#        num = num + 1

#devuelvePares=generaPares(10)

#print(next(devuelvePares))
#print("Aqui puede ir mas codigo")

#print(next(devuelvePares))
#print("Aqui puede ir mas codigo")

#print(next(devuelvePares))
#print("Aqui puede ir mas codigo")

#Instruccion yield from
#simplificar el codigo del generador en el caso de que se usen bucles anidados 

#Funcion para devolver ciudades 
'''
def devuelve_ciudades(*ciudades):   #un asterisco delante del argumento de la funcion indica que recibira una cantidad indeterminada de elementos y los recibira en formato de tupla
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Bogota", "Cali" , "Medellin")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
'''
def devuelve_ciudades(*ciudades):   #un asterisco delante del argumento de la funcion indica que recibira una cantidad indeterminada de elementos y los recibira en formato de tupla
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Bogota", "Cali" , "Medellin")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))









