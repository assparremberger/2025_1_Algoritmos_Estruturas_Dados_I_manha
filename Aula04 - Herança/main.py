import sys
from PyQt5.QtWidgets import QApplication

from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro
from TelaCategoria import TelaCategoria
from Categoria import Categoria

app = QApplication( sys.argv )

#telaVeiculo = TelaVeiculo( "Cadastro de Veículo")
#telaVeiculo.show()

categorias = []
telaCat = TelaCategoria("Adicionar Categorias", categorias )
#telaCat.show()

telaCarro = TelaCarro( "Cadastro de Carro", categorias, telaCat)
telaCarro.show()

#telaCat.telaCarro = telaCarro

sys.exit( app.exec_() )