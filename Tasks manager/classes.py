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

import pickle
import hashlib
from prettytable import PrettyTable


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.tarefas = []

    def cadastrar_usuario(self):
        try:
            ud = open('UserData.txt', 'r+')
            lines = ud.readlines()
            for line in lines:
                user = line.split()
                if self.nome == user[0]:
                    print('Este nome de usuário ja está sendo utilizado. tente novamente!')
                    return False
                ud.write(f'{self.nome} ')
                ud.write(hashlib.md5(f'{self.senha}\n'.encode("utf-8")).hexdigest())
            ud.close()
        except:
            ud = open('UserData.txt', 'x')
            ud.write(f'{self.nome} ')
            ud.write(hashlib.md5(f'{self.senha}\n'.encode("utf-8")).hexdigest())
            ud.close()
        print('Cadastro realizado com sucesso!')
        return True

    def login(self):
        try:
            with open('UserData.txt', 'r') as ud:
                lines = ud.readlines()
                for line in lines:
                    user = line.split()
                    if self.nome == user[0]:
                        if hashlib.md5(f'{self.senha}\n'.encode("utf-8")).hexdigest() == user[1]:
                            print('Login efeituado com sucesso!')
                            self.tarefas = Tarefa.carregar_tarefas(self.nome)
                            return True
        except:
            print('O usuário ou a senha estão incorretos. Tente novamente!')
            return False

    def inserir_tarefa(self, titulo, prioridade, descricao):
        self.tarefas.append(Tarefa(titulo, prioridade, descricao, self.nome))
        Tarefa.salvar_tarefas(self.nome, self.tarefas)

    def visualizar_tarefas(self):
        tabelaAlta = PrettyTable(['Id', 'Título', 'Prioridade', 'Descrição'])
        tabelaMedia = PrettyTable(['Id', 'Título', 'Prioridade', 'Descrição'])
        tabelaBaixa = PrettyTable(['Id', 'Título', 'Prioridade', 'Descrição'])
        self.tarefas = Tarefa.carregar_tarefas(self.nome)
        if self.tarefas:
            self.tarefas.sort(key=lambda x: str(x.identificador))
            for i in self.tarefas:
                if i.prioridade == 'Alta':
                    tarefa = {'Id': i.identificador, 'Título': i.titulo, 'Prioridade': i.prioridade,
                              'Descrição': i.descricao}

                    tabelaAlta.align['Id'] = 'l'
                    tabelaAlta.align['Título'] = 'l'
                    tabelaAlta.align['Prioridade'] = 'l'
                    tabelaAlta.align['Descrição'] = 'c'
                    tabelaAlta.padding_width = 3

                    tabelaAlta.add_row([tarefa['Id'], tarefa['Título'], tarefa['Prioridade'], tarefa['Descrição']])
                    print(tabelaAlta.get_string(sortby="Id"))
                    print('\n')
            for i in self.tarefas:
                if i.prioridade == 'Média':
                    tarefa = {'Id': i.identificador, 'Título': i.titulo, 'Prioridade': i.prioridade,
                              'Descrição': i.descricao}

                    tabelaMedia.align['Id'] = 'l'
                    tabelaMedia.align['Título'] = 'l'
                    tabelaMedia.align['Prioridade'] = 'l'
                    tabelaMedia.align['Descrição'] = 'c'
                    tabelaMedia.padding_width = 3

                    tabelaMedia.add_row([tarefa['Id'], tarefa['Título'], tarefa['Prioridade'], tarefa['Descrição']])
                    print(tabelaMedia.get_string(sortby="Id"))
                    print('\n')
            for i in self.tarefas:
                if i.prioridade == 'Baixa':
                    tarefa = {'Id': i.identificador, 'Título': i.titulo, 'Prioridade': i.prioridade,
                              'Descrição': i.descricao}

                    tabelaBaixa.align['Id'] = 'l'
                    tabelaBaixa.align['Título'] = 'l'
                    tabelaBaixa.align['Prioridade'] = 'l'
                    tabelaBaixa.align['Descrição'] = 'c'
                    tabelaBaixa.padding_width = 3

                    tabelaBaixa.add_row([tarefa['Id'], tarefa['Título'], tarefa['Prioridade'], tarefa['Descrição']])
                    print(tabelaBaixa.get_string(sortby="Id"))
                    print('\n')
        else:
            print('')
            print('Você não tem tarefas cadastradas no momento.')
            print('')

    def editar_tarefa(self, iden, nova_tarefa):
        for item in range(len(self.tarefas)):
            if self.tarefas[item].identificador == iden:
                self.tarefas[item] = nova_tarefa
        Tarefa.salvar_tarefas(self.nome, self.tarefas)

    def deletar_tarefa(self, iden):
        self.tarefas = list(filter(lambda tarefa: tarefa.identificador != iden, self.tarefas))
        Tarefa.salvar_tarefas(self.nome, self.tarefas)

class Tarefa:
    def __init__(self, titulo, prioridade, descricao, prefixo):
        self.titulo = titulo
        self.prioridade = prioridade
        self.descricao = Tarefa.controleCaracteres(descricao)
        self.identificador = Tarefa.idGeneration(prefixo)

    @staticmethod
    def controleCaracteres(descricao):
        desc = list(descricao.split())
        for i in range(len(desc)):
            if i != 0 and i % 10 == 0:
                desc[i] = desc[i] + '\n'
        return ' '.join(desc)

    @staticmethod
    def idGeneration(prefixo):
        filename = f'{prefixo}.bin'
        try:
            with open(filename, 'rb') as td:
                tamanho = pickle.load(td)
                if len(tamanho) == 0:
                    contador = 1
                else:
                    contador = len(tamanho) + 1
            return f'{contador:0>3}'
        except:
            contador = 1
            return f'{contador:0>3}'

    def __str__(self):
        return f'{self.identificador}\n{self.titulo}\n{self.prioridade}\n{self.descricao}'

    @staticmethod
    def salvar_tarefas(prefixo, tarefas):
        filename = f'{prefixo}.bin'
        try:
            with open(filename, 'wb') as td:
                pickle.dump(tarefas, td)
        except:
            with open(filename, 'x') as td:
                pickle.dump(tarefas, td)

    @staticmethod
    def carregar_tarefas(prefixo):
        filename = f'{prefixo}.bin'
        try:
            with open(filename, 'rb') as td:
                task = pickle.load(td)
                return task
        except:
            return []
