from No import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    
    def addNoInicio(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            nodo.prox = self.inicio
            self.inicio = nodo
        self.imprimir()

    def addNoFim(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            if self.inicio.prox is None:
                self.inicio.prox = nodo
            else:
                aux = self.inicio.prox
                while aux.prox is not None:
                    aux = aux.prox
                aux.prox = nodo
        self.imprimir()
    
    def imprimir(self):
        print("---------------------------------")
        if self.inicio is None:
            print( "Lista Encadeada está vazia!" )
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.prox
    
    def removerDoInicio(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            print( "Elemento Removido" )
        self.imprimir()

    def removerDoFim(self):
        if self.inicio is not None:
            if self.inicio.prox == None:
                self.inicio = None
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux.prox:
                    ant = aux
                    aux = aux.prox
                ant.prox = None
            print( "Elemento Removido" )
        self.imprimir()

    def remover(self, valor):
        print("Teste")
        if self.inicio != None:
            removeu = False
            if self.inicio.dado == valor:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux != None: 
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if removeu:
                    print( "Elemento ", valor, " removido")
                else:
                    print( "Elemento não encontrado")
        self.imprimir()