from Veiculo import Veiculo

class Carro( Veiculo ):

    def __init__(self, modelo, ano = 2025, qtd = 4, cat = None):
        super().__init__(modelo, ano)
        self.portas = qtd
        self.categoria = cat

    def __str__(self):
        return super().__str__() + "\nPortas: " + str(self.portas) + "\nCategoria: " + str( self.categoria )