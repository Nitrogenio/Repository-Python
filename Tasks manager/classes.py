import pickle
import hashlib
import os


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.tarefas = []

    def cadastrar_usuario(self):
        try:
            with open('UserData.txt', 'r') as ud:
                lines = ud.readlines()
                for line in lines:
                    user = line.split()
                    if self.nome == user[0]:
                        print('Este nome de usuário ja está sendo utilizado. tente novamente!')
                        return False
                ud.write(f'{self.nome} ')
                ud.write(hashlib.md5(f'{self.senha}'.encode("utf-8")).hexdigest())
        except:
            with open('UserData.txt', 'x') as ud:
                ud.write(f'{self.nome} ')
                ud.write(hashlib.md5(f'{self.senha}'.encode("utf-8")).hexdigest())
        return True

    def login(self):
        with open('UserData.txt', 'r') as ud:
            lines = ud.readlines()
            for line in lines:
                user = line.split()
                if self.nome == user[0]:
                    if hashlib.md5(f'{self.senha}'.encode("utf-8")).hexdigest() == user[1]:
                        print('Login efeituado com sucesso!')
                        self.tarefas = Tarefa.carregar_tarefas(self.nome)
                        return True
        print('O usuário ou a senha estão incorretos. Tente novamente!')
        return False

    def inserir_tarefa(self, titulo, prioridade, descricao):
        self.tarefas.append(Tarefa(titulo, prioridade, descricao))
        Tarefa.salvar_tarefas(self.nome, self.tarefas)

    def visualizar_tarefas(self):
        self.tarefas = Tarefa.carregar_tarefas(self.nome)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.tarefas.sort(key=lambda x: x.identificador)
        for i in self.tarefas:
            if i.prioridade == 'Alta':
                print('°' * 70)
                print('Id:', i.identificador)
                print('Titulo:', i.titulo)
                print('Prioridade:', i.prioridade)
                print('Descricao:', i.descricao)
                print('°' * 70)
        for i in self.tarefas:
            if i.prioridade == 'Média':
                print('°' * 70)
                print('Id:', i.identificador)
                print('Titulo:', i.titulo)
                print('Prioridade:', i.prioridade)
                print('Descricao:', i.descricao)
                print('°'*70)
        for i in self.tarefas:
            if i.prioridade == 'Baixa':
                print('°' * 70)
                print('Id:', i.identificador)
                print('Titulo:', i.titulo)
                print('Prioridade:', i.prioridade)
                print('Descricao:', i.descricao)
                print('°'*70)

    def editar_tarefa(self, iden, nova_tarefa):
        for item in range(len(self.tarefas)):
            if self.tarefas[item].identificador == iden:
                self.tarefas[item] = nova_tarefa
        Tarefa.salvar_tarefas(self.nome, self.tarefas)

    def deletar_tarefa(self, iden):
        self.tarefas = list(filter(lambda tarefa: tarefa.identificador != iden, self.tarefas))
        Tarefa.salvar_tarefas(self.nome, self.tarefas)

class Tarefa:
    def __init__(self, titulo, prioridade, descricao):
        self.titulo = titulo
        self.prioridade = prioridade
        self.descricao = descricao
        self.identificador = f'{Tarefa.contador:0>3}'
        Tarefa.contador += 1

    contador = 1

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
