from abc import ABC, abstractclassmethod
from os.path import isfile


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def atribuirConta(self, conta):
        self.conta = conta

    @staticmethod
    def salvarDados(cliente, conta):
        if not isfile('Dados.txt'):
            dados = open('Dados.txt', 'w')
            dados.write(f'Nome: {cliente.nome}; Agencia: {conta.agencia}; Saldo: {conta.saldo}; Conta: {conta.conta}\n')
            dados.close()
        else:
            dados = open('Dados.txt', 'a')
            dados.write(f'Nome: {cliente.nome}; Agencia: {conta.agencia}; Saldo: {conta.saldo}; Conta: {conta.conta}\n')
            dados.close()


class Conta(ABC):
    def __init__(self, agencia, saldo, conta):
        self.agencia = agencia
        self.saldo = saldo
        self.conta = conta

    def detalhes(self):
        print(f'Agencia: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Saldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    @abstractclassmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, saldo, conta, limite=1000):
        super().__init__(agencia, saldo, conta)
        self.limite = limite

    def sacar(self, valor):
        if valor < self.saldo and valor <= self.limite:
            self.saldo -= valor
        elif valor > self.saldo:
            print('Você não tem saldo suficiente.')
        elif valor > self.limite:
            print('Você não pode sacar valores acima do seu limite atual (1000)')
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Você não tem saldo suficiente.')
        else:
            self.saldo -= valor
        self.detalhes()


class Banco:
    def __init__(self):
        self.agencias = [1525, 3002]
        self.contas = []
        self.clientes = []

    def addCliente(self, cliente):
        self.clientes.append(cliente)

    def addContas(self, conta):
        self.contas.append(conta)

    def verificar(self, cliente):
        if cliente not in self.clientes:
            return

        if cliente.conta not in self.contas:
            return

        if cliente.conta.agencia not in self.agencias:
            return

        return True


#main
banco = Banco()

cliente1 = Cliente('Gabriel', 20)
cliente2 = Cliente('Karine', 18)
conta1 = ContaPoupanca(1525, 0, 32460)
conta2 = ContaCorrente(3002, 0, 32461)
cliente1.atribuirConta(conta1)
cliente2.atribuirConta(conta2)

banco.addContas(conta1)
banco.addCliente(cliente1)
banco.addContas(conta2)
banco.addCliente(cliente2)

if banco.verificar(cliente1):
    print('DEPOSITO:')
    cliente1.conta.depositar(1000)
    print('SAQUE')
    cliente1.conta.sacar(15)
    Cliente.salvarDados(cliente1, conta1)
else:
    print('Cliente não autenticado.')

print('###############################')

if banco.verificar(cliente2):
    print('DEPOSITO:')
    cliente2.conta.depositar(1000)
    print('SAQUE')
    cliente2.conta.sacar(15)
    Cliente.salvarDados(cliente2, conta2)
else:
    print('Cliente não autenticado.')

