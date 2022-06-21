"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""
bd = []
bd_secundario = []


def adicionar_tarefa(tarefa):
    bd.append(tarefa)


def listar_tarefas():
    print('\033[1;35mLista de Tarefas')
    for dados in bd:
        print(f'\033[1;36m-> {dados}')


def desfazer_tarefa():
    ultimo_indice_da_lista = bd[-1]
    bd_secundario.append(ultimo_indice_da_lista)
    bd.pop()


def refazer_tarefa():
    ultimo_indice_da_lista = bd_secundario[-1]
    bd.append(ultimo_indice_da_lista)
    bd_secundario.pop()


def acoes():
    print('\033[1;40m\033[1;97mLista de Ações:\033[0;0m ')
    print('\033[1;32m des\033[0;0m\033[;1m = desfazer a tarefa')
    print('\033[1;32m ref\033[0;0m\033[;1m = refazer a tarefa')
    print('\033[1;32m add\033[0;0m\033[;1m = adiciona uma nova tarefa')


acoes()

while True:
    entrada_de_dados = input('\n\033[1;34mDigite a ação desejada: ').lower()

    if entrada_de_dados == 'add':
        continua_lista_de_tarefas = 's'
        while True:
            if continua_lista_de_tarefas == 's':
                entrada_de_dados = input('\033[1;94mDigite a tarefa: ')
                adicionar_tarefa(entrada_de_dados)
                continua_lista_de_tarefas = input('Deseja adicionar outra tarefa ? (s / n): ').lower()
                if continua_lista_de_tarefas == 's':
                    continue
                elif continua_lista_de_tarefas == 'n':
                    break
                else:
                    continua_lista_de_tarefas = None
                    continue
            else:
                print(f'\033[1;31mDigite apenas s / n')
                continua_lista_de_tarefas = input('Deseja adicionar outra tarefa ? (s / n): ').lower()
        listar_tarefas()

    elif entrada_de_dados == 'des':
        if bd:
            desfazer_tarefa()
            listar_tarefas()
        else:
            print('Sem ações para fazer')

    elif entrada_de_dados == 'ref':
        if bd_secundario:
            refazer_tarefa()
            listar_tarefas()
        else:
            print('\033[1;33mSem ações para fazer')
    else:
        print('\033[1;31mDigite apenas ações que estão na lista de Ações')
        acoes()