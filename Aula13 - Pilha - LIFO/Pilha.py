from Livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None

    def add(self, autor, titulo, paginas):
            nodo = Livro(autor, titulo, paginas)
            if self.topo is None:
                self.topo = nodo
            else:
                nodo.prox = self.topo
                self.topo = nodo
            self.imprimir()     

    def remover(self):
        if self.topo is not None:
            self.topo = self.topo.prox
            print( "Elemento Removido" )
        self.imprimir()

    