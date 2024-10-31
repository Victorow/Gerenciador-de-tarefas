import json

class Tarefa:
    def __init__(self, descricao, prazo, prioridade):
        self.descricao = descricao
        self.prazo = prazo
        self.prioridade = prioridade
        self.concluida = False

    def para_dict(self):
        return {
            'descricao': self.descricao,
            'prazo': self.prazo,
            'prioridade': self.prioridade,
            'concluida': self.concluida
        }

    @staticmethod
    def de_dict(dados):
        tarefa = Tarefa(dados['descricao'], dados['prazo'], dados['prioridade'])
        tarefa.concluida = dados['concluida']
        return tarefa

class GerenciadorDeTarefas:
    def __init__(self, tarefas=None):
        self.tarefas = [Tarefa.de_dict(tarefa) for tarefa in tarefas] if tarefas else []

    def adicionar_tarefa(self, descricao, prazo, prioridade):
        nova_tarefa = Tarefa(descricao, prazo, prioridade)
        self.tarefas.append(nova_tarefa)

    def marcar_tarefa_como_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluida = True
            return True
        return False

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            return True
        return False

    def listar_tarefas_pendentes(self):
        print("\nTarefas Pendentes:")
        for i, tarefa in enumerate(self.tarefas):
            if not tarefa.concluida:
                print(f"{i}. {tarefa.descricao} - Prazo: {tarefa.prazo}, Prioridade: {tarefa.prioridade}")

    def listar_tarefas_concluidas(self):
        print("\nTarefas Concluídas:")
        for i, tarefa in enumerate(self.tarefas):
            if tarefa.concluida:
                print(f"{i}. {tarefa.descricao} - Prazo: {tarefa.prazo}, Prioridade: {tarefa.prioridade}")

    def listar_todas_as_tarefas(self):
        print("\nTodas as Tarefas:")
        for i, tarefa in enumerate(self.tarefas):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{i}. {tarefa.descricao} - Prazo: {tarefa.prazo}, Prioridade: {tarefa.prioridade}, Status: {status}")

    def filtrar_tarefas_por_prioridade(self, prioridade):
        print(f"\nTarefas com prioridade {prioridade}:")
        for i, tarefa in enumerate(self.tarefas):
            if tarefa.prioridade.lower() == prioridade.lower():
                status = "Concluída" if tarefa.concluida else "Pendente"
                print(f"{i}. {tarefa.descricao} - Prazo: {tarefa.prazo}, Status: {status}")

    def obter_tarefas(self):
        return [tarefa.para_dict() for tarefa in self.tarefas]
