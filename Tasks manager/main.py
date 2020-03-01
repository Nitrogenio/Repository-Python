#/*******************************************************************************
#Autor: Gabriel da Silva Barreto
#Componente Curricular: MI - Algoritmos
#Concluido em: 15/11/2019
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

from classes import *
import getpass
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_login():
    print('Entrou nesta tela por engano? Volte ao menu digitando 1.')
    engano = input('Ou aperte qualquer outra tecla: ')
    if engano == '1':
        return None
    while True:
        nome = input('Digite seu nome de usuário: ').upper()
        senha = getpass.getpass('Digite sua senha: ')
        user = Usuario(nome, senha)
        if user.login():
            return user
        print('Usuário e senha incorretos...')


def menu_cadastro():
    print('Entrou nesta tela por engano? Volte ao menu digitando 1.')
    engano = input('Ou aperte qualquer outra tecla: ')
    if engano == '1':
        return None
    while True:
        nome = input('Digite seu nome de usuário: ').upper()
        senha = getpass.getpass('Digite sua senha: ')
        confirmando = getpass.getpass('Confirme sua senha: ')
        if senha == confirmando:
            user = Usuario(nome, senha)
            if user.cadastrar_usuario():
                return user
        print('As senhas estão diferentes..')


def cadastrar_tarefas(user):
    print('Entrou nesta tela por engano? Volte ao menu digitando 1.')
    engano = input('Ou aperte qualquer outra tecla: ')
    if engano == '1':
        return None
    titulo = input('Digite o título da tarefa: ')
    print('Prioridades:\n'
          '[1] Baixa\n'
          '[2] Média\n'
          '[3] Alta')
    prioridade = input('Digite o Nº da opção de prioridade: ')
    if prioridade == '1':
        prioridade = 'Baixa'
    elif prioridade == '2':
        prioridade = 'Média'
    elif prioridade == '3':
        prioridade = 'Alta'
    else:
        print('Digite uma opção válida.')
    descricao = input('Digite a descrição da tarefa: ')
    user.inserir_tarefa(titulo, prioridade, descricao)


def visualizar_tarefas(user):
    print('Entrou nesta tela por engano? Volte ao menu digitando 1.')
    engano = input('Ou aperte qualquer outra tecla: ')
    if engano == '1':
        return None
    user.visualizar_tarefas()


def alterar_tarefas(user):
    print('Entrou nesta tela por engano? Volte ao menu digitando 1.')
    engano = input('Ou aperte qualquer tecla: ')
    if engano == '1':
        return None
    user.visualizar_tarefas()
    iden = input('Digite o id da tarefa que você quer editar: ')
    titulo = input('Digite o título da tarefa: ')
    print('Prioridades:\n'
          '[1] Baixa\n'
          '[2] Média\n'
          '[3] Alta')
    prioridade = input('Digite o Nº da opção de prioridade: ')
    descricao = input('Digite a descrição da tarefa: ')
    nova_tarefa = Tarefa(titulo, prioridade, descricao)
    user.editar_tarefa(iden, nova_tarefa)


def excluir_tarefa(user):
    print('Entrou nesta tela por engano? Volte ao menu digitando 1.')
    engano = input('Ou aperte qualquer tecla: ')
    if engano == '1':
        return None
    user.visualizar_tarefas()
    iden = input('Digite o id da tarefa que você quer editar: ')
    user.deletar_tarefa(iden)


def menu_tarefas(user):
    while True:
        print('')
        print('[1] Cadastrar tarefa.')
        print('[2] Visualizar tarefas')
        print('[3] Alterar tarefa')
        print('[4] Excluir tarefa')
        print('[5] Sair')
        print('')
        opcao = input('Digite o Nº da opção que você deseja: ')
        if opcao == '1':
            clear()
            cadastrar_tarefas(user)
        elif opcao == '2':
            clear()
            visualizar_tarefas(user)
        elif opcao == '3':
            clear()
            alterar_tarefas(user)
        elif opcao == '4':
            clear()
            excluir_tarefa(user)
        elif opcao == '5':
            return None
        else:
            print('Digite uma opção válida.')


def menu():
    opcao = 3
    while opcao != '3':
        print('')
        print('[1] Usuário novo? Digite 1 e cadastre-se.')
        print('[2] Já tem um cadastro? Digite 2 para entrar no sistema.')
        print('[3] Deseja sair do sistema? Digite 3...')
        print('')
        opcao = input('Digite aqui: ')
        if opcao == '1':
            clear()
            user = menu_cadastro()
            if user:
                clear()
                menu_tarefas(user)
        elif opcao == '2':
            clear()
            user = menu_login()
            if user:
                clear()
                menu_tarefas(user)
        elif opcao == '3':
            sys.exit('Saindo do sistema...')
        else:
            print('Digite uma opção válida')


menu()
