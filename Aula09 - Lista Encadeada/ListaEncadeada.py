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
        
