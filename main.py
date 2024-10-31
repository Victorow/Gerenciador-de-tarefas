import json
import os
from tasks.tasks import GerenciadorDeTarefas

def carregar_tarefas():
    if os.path.exists('data/tarefas.json'):
        with open('data/tarefas.json', 'r') as file:
            return json.load(file)
    return []

def salvar_tarefas(tarefas):
    with open('data/tarefas.json', 'w') as file:
        json.dump(tarefas, file, indent=4)

def main():
    gerenciador = GerenciadorDeTarefas(carregar_tarefas())
    
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Marcar tarefa como concluída")
        print("3. Listar tarefas pendentes")
        print("4. Listar tarefas concluídas")
        print("5. Remover tarefa")
        print("6. Filtrar tarefas por prioridade")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Descrição da tarefa: ")
            prazo = input("Prazo (YYYY-MM-DD): ")
            prioridade = input("Prioridade (alta, média, baixa): ")
            gerenciador.adicionar_tarefa(descricao, prazo, prioridade)
            salvar_tarefas(gerenciador.obter_tarefas())
            print("Tarefa adicionada com sucesso!")

        elif escolha == '2':
            gerenciador.listar_tarefas_pendentes()
            indice_tarefa = int(input("Escolha o índice da tarefa a marcar como concluída: "))
            if gerenciador.marcar_tarefa_como_concluida(indice_tarefa):
                salvar_tarefas(gerenciador.obter_tarefas())
                print("Tarefa marcada como concluída com sucesso!")
            else:
                print("Índice de tarefa inválido!")

        elif escolha == '3':
            while True:
                gerenciador.listar_tarefas_pendentes()
                continuar = input("Deseja listar novamente as tarefas pendentes? (s/n): ")
                if continuar.lower() != 's':
                    break

        elif escolha == '4':
            while True:
                gerenciador.listar_tarefas_concluidas()
                continuar = input("Deseja listar novamente as tarefas concluídas? (s/n): ")
                if continuar.lower() != 's':
                    break

        elif escolha == '5':
            gerenciador.listar_todas_as_tarefas()
            indice_tarefa = int(input("Escolha o índice da tarefa a remover: "))
            if gerenciador.remover_tarefa(indice_tarefa):
                salvar_tarefas(gerenciador.obter_tarefas())
                print("Tarefa removida com sucesso!")
            else:
                print("Índice de tarefa inválido!")

        elif escolha == '6':
            prioridade = input("Filtrar por prioridade (alta, média, baixa): ")
            gerenciador.filtrar_tarefas_por_prioridade(prioridade)

        elif escolha == '7':
            print("Saindo do gerenciador de tarefas.")
            break

        else:
            print("Opção inválida!")

if _name_ == "_main_":
    main()
