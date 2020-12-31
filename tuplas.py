miTupla=("elem1", 5, 78.35, "elem4", "elem1") #estructura de una tupla

print(miTupla[0])
#Accediendo a porciones de listas 

print(miTupla[0:3]) 


#Funcion in devuelve true o false si el elemento se encuentra en la lista

print("Joseph" in miTupla)

#Conversion de tuplas a listas y viceversa

#Metodo list 

miLista = list(miTupla)

print(miLista)

print(type(miLista))

#Metodo tuple

miTupla2 = tuple(miLista)

print(miTupla2)

#Metodo count cuantas veces se encuentra un elemeto en una tupla

print(miTupla2.count("elem1"))

#Metodo len imprime el tamaño de una tupla

print(len(miTupla))


#Tuplas unitarias

miTuplaUnitaria = ("Unitaria",)

print(miTuplaUnitaria)


#Empaquetado de Tupla

miTupla6=("Joseph", 14, 4, 1990)
nombre, dia, mes, agno = miTupla6
print(nombre)
print(dia)
print(mes)
print(agno)

#Desempaquetado de Tupla








