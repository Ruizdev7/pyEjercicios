MIDICCIONARIO = {"Colombia":"Bogota", "Francia":"Paris", "UK":"Londres"} #Estructura del diccionario

print(MIDICCIONARIO["Colombia"]) #Imprimiendo un valor del diccionario
print(MIDICCIONARIO) #Imprimiendo la totalidad del diccionario

MIDICCIONARIO["Italia"]="Lisboa"  #Asignando nuevos elementos al diccionario

print(MIDICCIONARIO)

MIDICCIONARIO["Italia"]="Roma"   #Sobreescribiendo un elemento del diccionario

print(MIDICCIONARIO)


#Metodo del

del MIDICCIONARIO["Francia"]

print(MIDICCIONARIO)    # Eliminando elementos mediante el metodo del 

MIDICCIONARIO2= {"Ruizdev":7,10:"Diego Maradona","Alemania":"Berlin"} #Mezclando diferentes tipos de clave y valor

print(MIDICCIONARIO2)

#Asignando valores al diccionario mediante el uso de tuplas

miTupla=["España","Francia","UK","Alemania"]

MIDICCIONARIO3={miTupla[0]:"Madrid", miTupla[1]:"Paris"}

print(MIDICCIONARIO3["Francia"])

MIDICCIONARIO4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}

print(MIDICCIONARIO4)

print(MIDICCIONARIO4["Anillos"])

#Metodos interesantes

#Metodo keys-values-len

print(MIDICCIONARIO4.keys())
print(MIDICCIONARIO4.values())
print(len(MIDICCIONARIO4))
print(MIDICCIONARIO4)
