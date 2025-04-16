import sys
from PyQt5.QtWidgets import *
from Categoria import Categoria
from TelaCarro import TelaCarro

class TelaCategoria( QMainWindow ):
    def __init__(self, titulo = "Tela de Categoria", categorias = [], telaCar = None ):
        self.telaCarro = telaCar
        self.categorias = categorias
        super().__init__()
        self.setWindowTitle( titulo )
        self.setGeometry( 300, 200, 150, 150 )
        self.layout = QVBoxLayout()
        self.definirLayout()

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect( self.salvar )
        self.layout.addWidget( self.btnSalvar)
        
        container = QWidget()
        container.setLayout( self.layout )
        self.setCentralWidget( container )
    
    def salvar(self):
        nome = self.txtNome.text() 
        if nome != "" :
            cat = Categoria( nome )
            self.categorias.append( cat )
            QMessageBox.information(self, "Categoria Salva", str(cat) )
            if self.telaCarro is not None:
                self.telaCarro.carregarCategorias()
            self.txtNome.setText( "" )
            self.hide()


    def definirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.txtNome = QLineEdit(self)
        self.layout.addWidget( self.lblNome)
        self.layout.addWidget( self.txtNome )
