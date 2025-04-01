import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox

class GerenciadorBibliotecas(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setWindowTitle('Gerenciador de Bibliotecas')
        self.setGeometry(100, 100, 600, 400)

        # Layout principal
        self.layout = QVBoxLayout()

        # Título
        self.titulo_label = QLabel('Escolha um livro para emprestar:')
        self.layout.addWidget(self.titulo_label)

        # ComboBox para listar os livros disponíveis
        self.combo_livros = QComboBox()
        self.combo_livros.addItem('O Senhor dos Anéis')
        self.combo_livros.addItem('Dom Quixote')
        self.combo_livros.addItem('Guerra e Paz')
        self.combo_livros.addItem('Cem Anos de Solidão')
        self.combo_livros.addItem("O Senhor dos Anéis")
        self.combo_livros.addItem("Dom Quixote")
        self.combo_livros.addItem("Guerra e Paz")
        self.combo_livros.addItem("Cem Anos de Solidão")
        self.combo_livros.addItem("O Hobbit")
        self.combo_livros.addItem("O Retrato de Dorian Gray")
        self.combo_livros.addItem("Frankenstein")
        self.combo_livros.addItem("Drácula")
        self.combo_livros.addItem("O Conde de Monte Cristo")
        self.combo_livros.addItem("Ulisses")
        self.combo_livros.addItem("Em Busca do Tempo Perdido")
        self.combo_livros.addItem("A Metamorfose")
        self.layout.addWidget(self.combo_livros)

        # Campos para nome e telefone
        self.nome_label = QLabel('Digite seu nome:')
        self.layout.addWidget(self.nome_label)
        self.nome_input = QLineEdit()
        self.layout.addWidget(self.nome_input)

        self.telefone_label = QLabel('Digite seu telefone:')
        self.layout.addWidget(self.telefone_label)
        self.telefone_input = QLineEdit()
        self.layout.addWidget(self.telefone_input)

        # Botão de Emprestar
        self.emprestar_button = QPushButton('Emprestar Livro')
        self.emprestar_button.clicked.connect(self.emprestar_livro)
        self.layout.addWidget(self.emprestar_button)

        # Exibe a mensagem
        self.mensagem_label = QLabel('')
        self.layout.addWidget(self.mensagem_label)

        # Define o layout
        self.setLayout(self.layout)

    def emprestar_livro(self):
        # Lógica para registrar o nome e telefone e "emprestar" o livro
        nome = self.nome_input.text()
        telefone = self.telefone_input.text()
        livro_escolhido = self.combo_livros.currentText()

        if nome and telefone:
            self.mensagem_label.setText(f'O livro "{livro_escolhido}" foi emprestado a {nome}, telefone: {telefone}.')
        else:
            self.mensagem_label.setText('Por favor, preencha todos os campos.')

# Inicializa o aplicativo PyQt
app = QApplication(sys.argv)
janela = GerenciadorBibliotecas()
janela.show()
sys.exit(app.exec_())
