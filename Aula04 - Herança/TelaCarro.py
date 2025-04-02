import sys
from PyQt5.QtWidgets import *
from Carro import Carro
from TelaVeiculo import TelaVeiculo

class TelaCarro( TelaVeiculo ):

    def __init__(self, titulo = "Tela de Carro"):
        super().__init__(titulo)

    def definirLayout(self):
        super().definirLayout()
        self.lblPortas = QLabel( "Qtd Portas: ")
        self.txtPortas = QLineEdit(self)
        self.layout.addWidget( self.lblPortas )
        self.layout.addWidget( self.txtPortas )

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