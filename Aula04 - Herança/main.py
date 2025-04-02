import sys
from PyQt5.QtWidgets import QApplication

from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro

app = QApplication( sys.argv )

telaVeiculo = TelaVeiculo( "Cadastro de Veículo")
telaVeiculo.show()

telaCarro = TelaCarro( "Cadastro de Carro")
telaCarro.show()

sys.exit( app.exec_() )