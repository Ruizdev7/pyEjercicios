#Errores que ocurren durante la ejecución del programa, la sintaxis de código es correcta pero durante la ejecución ha ocurrido algo inesperado

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1,num2):
    
    try:
    
        return num1/num2
    
    except ZeroDivisionError:
        
        print("No se puede dividir entre zero")
        return "Operación errónea"

while True:                    ####USO DE CICLOS INFINITOS PARA REINTENTOS

    try:
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))

        break

    except ValueError:
        print("Los valores introducidos no son correctos, intentalo de nuevo")
                     
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
    print(suma(op1,op2))

elif operacion=="resta":
    print(resta(op1,op2))

elif operacion=="multiplica":
    print(multiplica(op1,op2))

elif operacion=="divide":
    print(divide(op1,op2))

else:
    print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")


#Usus de la captura de varias exepciones y la funcionalidad finally
