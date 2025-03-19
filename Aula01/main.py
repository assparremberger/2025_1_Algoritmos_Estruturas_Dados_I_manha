# Construa uma classe chamada Carro que possui os 
#atributos modelo, ano e kilometragem.

#Esta classe também deve conter uma método para 
#incrementar a quilometragem e um método para 
#imprimir os dados de todos atributos do objeto carro

class Carro:

    def __init__(self, modelo = None, ano = 2025):
        self.modelo = modelo
        self.ano = ano
        self.__kilometragem = 0

    def incrementar(self, km):
        if km > 0:
            self.__kilometragem += km

    def setKM(self, km):
        if km > self.__kilometragem:
            self.__kilometragem = km

    def __str__(self):
        txt = "Modelo: " + self.modelo
        txt += "\nAno: " + str( self.ano )
        txt += "\nKilometragem: " + str( self.__kilometragem )
        return txt 

    def imprimir(self):
        print( self )


x = Carro("Doblo", 2025)
print( x )