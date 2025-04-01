class Tarefas:
    def __init__(self, titulo, descricao, status):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "pendente"
    def concluido(self):
        self.status = "concluida"
class ListarTarefas:
    def __init__(self, lista_tarefas):
        self.lista_tarefas = ["Lavar os pratos", "Passar roupas", "Tirar o lixo", "Limpar o chão"]
        print(lista_tarefas)
