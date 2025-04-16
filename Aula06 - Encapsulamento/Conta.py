class Conta:

    logado = True
    tarifa = 1.99

    def __init__(self):
        self.__saldo = 0.0

    def getSaldo(self):
        if self.logado:
            return self.__saldo
        else:
            return None
    
    def setSaldo( self, valor):
        if valor > self.__saldo :
            self.__saldo = valor
    
    @property
    def saldo(self):
        if self.logado:
            return self.__saldo
        else:
            return None
        
    @saldo.setter
    def saldo( self, valor):
        if valor > self.__saldo :
            self.__saldo = valor
        else:
            print( "Valor não permitido!")

    def __descontarTarifa(self):
        self.__saldo -= self.tarifa

    def sacar(self, valor):
        if self.__saldo >= valor + self.tarifa :
            self.__saldo -= valor
            self.__descontarTarifa()
        else:
            print( "Valor não permitido!")



