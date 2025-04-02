class Veiculo:
    def __init__(self, modelo, ano = 2025):
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return self.modelo + "\nAno: " + str(self.ano)