from datetime import datetime as dt
import random as rd

def menu():
    print("1 - Criar Conta")
    print("2 - Listar Contas")
    print("3 - Sacar Valor")
    print("4 - Depositar Valor")
    print("5 - Transferir Valor")
    print("6 - Excluir Conta")
    print("7 - Historico")
    print("0 - Sair")
    op = int(input("Digite uma das opções acima: "))
    return op

class Conta:
    #Declarando Todas as Variaveis da Class conta e as deixadno como Private 
    def __init__(self, nome, saldo=0):
        self._nome = nome
        self._numero = ''.join(str(rd.randint(0, 9)) for _ in range(3))
        self._saldo = saldo
        self.historico = []

    @property
    def nome(self):
        return self._nome
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, value):
        print("Erro: Não é possível mudar o número da conta!")

    #adicionado a lista do historico todo tipo de transação
    def adicionar_historico(self, transacao):
        self.historico.append(transacao)

    def imprimir_historico(self):
        for transacao in self.historico:
            print(transacao.detalhes())

class Acoes:
    #declarando o dicionario das contas
    def __init__(self):
        self.contas = {}

    #Função para cadastrar conta
    def cadastrar(self, nome):
        nova_conta = Conta(nome)
        self.contas[nova_conta.numero] = nova_conta
        print(f"Conta {nova_conta.numero} cadastrada com sucesso!")
    #Função para Listar as contas
    def listar(self):
        for numero, conta in self.contas.items():
            print(f"Conta: {numero}, Nome: {conta.nome}, Saldo: {conta._saldo}")
    #Função para buscar conta 
    def _busca_conta(self, numero):
        return self.contas.get(numero, None)
    #Função para sacar dinheiro da conta
    def sacar(self, numero, valor):
        conta = self._busca_conta(numero)
        if conta and conta._saldo >= valor:
            conta._saldo -= valor
        # ao sacar a class historico vai pegar o valor e numero da conta da acao e a variavel transacao vai armazenar isso no historico das class Conta
            transacao = Historico("saque", valor, conta_o=conta)
            conta.adicionar_historico(transacao)
            print(f"Valor R${valor} sacado!")
        else:
            print("Saldo insuficiente ou conta não encontrada!")

    def depositar(self, numero, valor):
        conta = self._busca_conta(numero)
        if conta:
            conta._saldo += valor
            # ao sacar a class historico vai pegar o valor e numero da conta da acao e a variavel transacao vai armazenar isso no historico das class Conta
            transacao = Historico("deposito", valor, conta_o=conta)
            conta.adicionar_historico(transacao)
            print(f"Valor R${valor} depositado!")
        else:
            print("Conta não encontrada!")

    def transferir(self, numero_o, numero_d, valor):
        conta_o = self._busca_conta(numero_o)
        conta_d = self._busca_conta(numero_d)
        if conta_o and conta_d and conta_o._saldo >= valor:
            conta_o._saldo -= valor
            conta_d._saldo += valor
            # ao sacar a class historico vai pegar o valor e numero da conta da acao e a variavel transacao vai armazenar isso no historico das class Conta
            # Nesse caso sera feito a adicao nos 2 historicos da mesma transação
            transacao = Historico("transferencia", valor, conta_o=conta_o, conta_d=conta_d)
            conta_o.adicionar_historico(transacao)
            conta_d.adicionar_historico(transacao)
            print(f"Transferência de R${valor} da Conta {numero_o} para Conta {numero_d}")
        else:
            print("Saldo insuficiente ou conta não encontrada!")

    def excluir(self, numero):
        conta = self._busca_conta(numero)
        if conta:
            del self.contas[numero]
            print(f"Conta {numero} excluída com sucesso!")
        else:
            print("Conta não encontrada!")
class Historico:
    def __init__(self, tipo, valor, conta_o=None, conta_d=None):
        self.tipo = tipo
        self.valor = valor
        self.conta_o = conta_o
        self.conta_d = conta_d
        self.data = dt.now()

    def detalhes(self):
        if self.tipo == "transferencia":
            return f"{self.data} - {self.tipo} de R${self.valor} da Conta {self.conta_o.numero} para Conta {self.conta_d.numero}"
        else:
            return f"{self.data} - {self.tipo} de R${self.valor} na Conta {self.conta_o.numero}"

def main():
    acoes = Acoes()
    while True:
        op = menu()
        if op == 1:
            nome = input("Digite o nome do titular da conta: ")
            acoes.cadastrar(nome)
        elif op == 2:
            acoes.listar()
        elif op == 3:
            numero = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a ser sacado: "))
            acoes.sacar(numero, valor)
        elif op == 4:
            numero = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a ser depositado: "))
            acoes.depositar(numero, valor)
        elif op == 5:
            numero_o = input("Digite o número da conta de origem: ")
            numero_d = input("Digite o número da conta de destino: ")
            valor = float(input("Digite o valor a ser transferido: "))
            acoes.transferir(numero_o, numero_d, valor)
        elif op == 6:
            numero = input("Digite o número da conta a ser excluída: ")
            acoes.excluir(numero)
        elif op == 7:
            numero = input("Digite o número da conta: ")
            conta = acoes._busca_conta(numero)
            if conta:
                conta.imprimir_historico()
            else:
                print("Conta não encontrada!")
        elif op == 0:
            break
        else:
            print("Opção inválida!")

main()