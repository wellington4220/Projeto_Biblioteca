class Livros:
    def __init__(self,titulo,autor,paginas,status):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.status = status
    def emprestar(self):
        if self.status == "disponivel":
            self.status = "emprestado"
        else:
            print("Este livro já foi emprestado")
    def devolver(self):
        if self.status == "emprestado":
            self.status = "disponivel"
        else:
            print("Este livro já foi devolvido")
    def registrar_usuário(self):
        nome = input("Digite seu nome")
        telefone = input("Digite aqui seu telefone")
        self.usuario = {"nome": nome, "telefone": telefone}

    def informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de Páginas: {self.paginas}")
        print(f"Status: {self.status}")
#Criando os objetos dentro de uma lista
lista_de_livros = [
    Livros("O Senhor dos Anéis", "J.R.R. Tolkien", 1200, "disponivel"),
    Livros("Dom Quixote", "Miguel de Cervantes", 1000, "emprestado"),
    Livros("Guerra e Paz", "Lev Tolstói", 1400, "disponivel"),
    Livros("Cem Anos de Solidão", "Gabriel Márquez", 400, "disponivel"),
    Livros("O Grande Gatsby", "F. Scott Fitzgerald", 200, "emprestado"),
    Livros("A Bíblia", "Diversos autores", 1200, "disponivel"),
    Livros("O Hobbit", "J.R.R. Tolkien", 320, "emprestado"),
    Livros("O Retrato de Dorian Gray", "Oscar Wilde", 250, "emprestado"),
    Livros("Frankenstein", "Mary Shelley", 280, "emprestado"),
    Livros("Drácula", "Bram Stoker", 500, "emprestado"),
    Livros("O Conde de Monte Cristo", "Alexandre Dumas", 1300, "emprestado"),
    Livros("Ulisses", "James Joyce", 730, "disponivel"),
    Livros("Em Busca do Tempo Perdido", "Marcel Proust", 4200, "disponivel"),
    Livros("A Metamorfose", "Franz Kafka", 120, "disponivel")
]
for livros in lista_de_livros:
    livros.informacoes()

def livros_disponiveis():
    for livros in lista_de_livros:
        if livros.status == "disponivel":  # Verifica se o livro está disponível
            livros.informacoes()  # Exibe as informações do livro
#exibindo so os livros disponiveis
livros_disponiveis()
#pedir ao usuario que escolha um livro
titulo_escolhido = input("Qual destes livros deseja adquirir?: ")
#retorna livros disponíveis
def livros_disponiveis():
    livros_disponiveis_lista = []
    for livro in lista_de_livros:
        if livro.status == "disponivel":
            livros_disponiveis_lista.append(livro)  # Adiciona o livro à lista de disponíveis
    return livros_disponiveis_lista  # Retorna a lista de livros disponíveis

# Agora você pode iterar sobre os livros disponíveis
for livro in livros_disponiveis():
    livro.informacoes()  # Exibe as informações de cada livro disponível

for livro in lista_de_livros:
    if livro.titulo == titulo_escolhido:
        if livro.status == "disponivel":
            # Aqui você adiciona o código para quando o livro estiver disponível
            print(f"O livro {livro.titulo} está disponível para empréstimo.")
        else:
            # Aqui você adiciona o código para quando o livro não estiver disponível
            print(f"O livro {livro.titulo} não está disponível no momento.")
#armazenando o livro escolhido pelo usuario





