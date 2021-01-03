class Coche():
    
    def __init__(self):

        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):

            return "El coche esta en marcha"
        
        elif (self.__enmarcha and chequeo==False):

            return "Algo ha ido mal en el chequeo"

        else:
            
            return "El coche esta parado"        

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas ", "Un ancho de ", self.__anchoChasis, "y un largo de ", self.__largoChasis)


    def __chequeo_interno(self):
        print("Realizando cheque interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("*****************Se crea el segundo objeto******************************")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

#print(miCoche.__chequeo_interno)

