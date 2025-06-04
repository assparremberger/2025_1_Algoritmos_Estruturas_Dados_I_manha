from No import No
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, valor):
        nodo = No( valor )
        if self.inicio is None:
            self.inicio = nodo
            self.fim = nodo
        elif nodo.dado < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio.ant = nodo
            self.inicio = nodo
        elif nodo.dado > self.fim.dado:
            nodo.ant = self.fim
            self.fim.prox = nodo
            self.fim = nodo
        else:
            antTestado = self.inicio
            aux = self.inicio.prox
            while aux:
                if nodo.dado < aux.dado:
                    nodo.prox = aux
                    nodo.ant = antTestado  # nodo.ant = aux.ant
                    antTestado.prox = nodo # aux.ant.prox = nodo
                    aux.ant = nodo
                    break
                else:
                    antTestado = aux
                    aux = aux.prox
        #   if aux == None:
        #       nodo.ant = self.fim
        #       self.fim.prox = nodo
        #       self.fim = nodo  
        self.imprimir()  

    def imprimir(self):
        print("--------Lista Duplamente Encadeada-----")
        if self.inicio is None:
            print( "Lista está vazia!" )
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.prox     

    def imprimirReverso(self):
        print("--------Lista Duplamente Encadeada Reversa-----")
        if self.fim is None:
            print( "Lista está vazia!" )
        else:
            aux = self.fim
            while aux :
                print( aux.dado )
                aux = aux.ant  

    def remover(self, valor):
        if self.inicio != None:
            removeu = False
            if self.inicio.dado == valor:
                self.inicio = self.inicio.prox
                if self.inicio == None:
                    self.fim = None
                else:
                    self.inicio.ant = None
                removeu = True
            else:
                antTestado = self.inicio
                aux = self.inicio.prox
                while aux != None: 
                    if valor == aux.dado:
                        antTestado.prox = aux.prox
                        if aux.prox is not None:
                            aux.prox.ant = antTestado
                        else:
                            self.fim = antTestado
                        removeu = True
                        break
                    else:
                        antTestado = aux
                        aux = aux.prox
                if removeu:
                    print( "Elemento ", valor, " removido")
                else:
                    print( "Elemento não encontrado")
        self.imprimir()