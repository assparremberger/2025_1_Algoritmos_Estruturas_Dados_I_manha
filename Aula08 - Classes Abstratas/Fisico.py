from Cliente import Cliente

class Fisico( Cliente ):

    def __init__(self, nome, cpf = None):
        super().__init__(nome)
        self.cpf = cpf

    def __str__(self):
        return super().__str__() + "\nCPF: " + self.cpf
    
    def cadastrar(self):
        self.nome = input("Digite o nome: ")
        self.cpf = input("Digite o CPF: ")