miLista=["elem1", 5, 78.35, "elem4"] #estructura de una lista

print(miLista[0])
print(miLista[1])
print(miLista[2])
print(miLista[3])
print(miLista[-1])
print(miLista[-2])
print(miLista[-3])

#Accediendo a porciones de listas 


print(miLista[0:3]) 
print(miLista[:3])
print(miLista[1:2])
print(miLista[2:])

#Funcion append agrega al final de la lista

miLista.append("Joseph")
print(miLista)

#Funcion insert agrega a la lista indicando el indice

miLista.insert(2, "Prueba de Insercion")

print(miLista)

#Funcion extend permite concatenar listas agregando a la original

miLista.extend(["extend1","extend2","extend3" ])
print(miLista)

#Funcion index permite saber cual es el indice de un elemento dentro de la lista

print(miLista.index("Joseph"))

#Funcion in devuelve true o false si el elemento se encuentra en la lista

print("Joseph" in miLista)

#Eliminando elementos

#Funcion remove elimina elemento entre parentesis de la lista 

miLista.remove("elem4")

print(miLista[:])

#Funcion pop Elimina el ultimo elemento de la lista

miLista.pop()

print(miLista)

#Operador mas para sumar el contenido de dos listas diferentes

miLista2 = ["Sandra", "Lucia"]

miLista3 = miLista + miLista2

print(miLista3)

#Operador por permite repetir el contenido de la lista por el numero de veces multiplicado

miLista4 = miLista3 * 3

print(miLista4)
