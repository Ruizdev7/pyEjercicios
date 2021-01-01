print("Programa de evaluacion de notas de alumnos")

nota_alumno = int(input("Ingrese una nota de 1 a 5: "))

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(nota_alumno))

