import sys
from PyQt5.QtWidgets import *
from Carro import Carro
from TelaVeiculo import TelaVeiculo
from TelaCategoria import TelaCategoria

class TelaCarro( TelaVeiculo ):

    def __init__(self, titulo = "Tela de Carro", categorias = [], telaCat = None ):
        self.telaCategorias = telaCat
        self.listaCategorias = categorias
        super().__init__(titulo)
        

    def definirLayout(self):
        super().definirLayout()
        self.lblPortas = QLabel( "Qtd Portas: ")
        self.txtPortas = QLineEdit(self)
        self.layout.addWidget( self.lblPortas )
        self.layout.addWidget( self.txtPortas )

        self.lblCategoria = QLabel("Categoria:")
        self.layout.addWidget( self.lblCategoria)

        self.cmbCategoria = QComboBox(self)
        self.cmbCategoria.addItem( "Selecione...", None)
        for cat in self.listaCategorias:
            self.cmbCategoria.addItem( cat.nome , cat)
        self.layout.addWidget(self.cmbCategoria )

        self.btnAddCategoria = QPushButton("Adicionar Categoria", self)
        self.btnAddCategoria.clicked.connect( self.abrirTelaCategoria )
        self.layout.addWidget( self.btnAddCategoria)


    def abrirTelaCategoria(self):
        self.telaCategorias.show()

    def salvar(self):
        modelo = self.txtModelo.text() 
        if modelo != "" :
            ano = self.txtAno.text()
            valor = None
            if ano != "":
                valor = int( ano )

            portas = self.txtPortas.text()
            vPortas = None
            if portas != "":
                vPortas = int( portas ) 
            carro = Carro(modelo, ano, vPortas)
            QMessageBox.information(self, "Carro Salvo", str(carro) )