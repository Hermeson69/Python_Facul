from datetime import datetime

def menu():
    print("1 - Cadastrar Conta")
    print("2 - Sacar Dinheiro")
    print("3 - Ver Extrato")
    print("4 - Depositar")
    print("5 - Transferir")
    print("6 - Modificar Nome do Titular")
    op = int(input("Digite uma das Opções Acima: "))
    return op

class Conta:
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = 0
    #"Somente deixando privado"
    @property
    def titular(self):
        return self._titular
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, _):
        print("Erro: Número da conta não pode ser alterado!")

class Acoes():
    def __init__(self):
        self.contas = []

    def cadastrar_conta(self, numero, titular):
        nova_conta = Conta(numero, titular, 0)
        self.contas.append(nova_conta)
        print(f"Conta {numero} cadastrada com sucesso!")

    def sacar(self, numero, valor):
        conta = self._buscar_conta(numero)
        if conta and conta._saldo >= valor:
            conta._saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou conta não encontrada.")

    def ver_extrato(self, numero):
        conta = self._buscar_conta(numero)
        if conta:
            print(f"Extrato da conta {numero}: Saldo atual é R${conta._saldo}")
        else:
            print("Conta não encontrada.")

    def depositar(self, numero, valor):
        conta = self._buscar_conta(numero)
        if conta:
            conta._saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Conta não encontrada.")

    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self._buscar_conta(numero_origem)
        conta_destino = self._buscar_conta(numero_destino)
        if conta_origem and conta_destino and conta_origem._saldo >= valor:
            conta_origem._saldo -= valor
            conta_destino._saldo += valor
            print(f"Transferência de R${valor} realizada com sucesso!")
        else:
            print("Saldo insuficiente ou conta não encontrada.")

    def modificar_nome_titular(self, numero, novo_titular):
        conta = self._buscar_conta(numero)
        if conta:
            conta.titular = novo_titular
            print(f"Nome do titular da conta {numero} alterado com sucesso!")
        else:
            print("Conta não encontrada.")

    def _buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None
    
class Transacao:
    def __init__(self, tipo, valor, conta_origem=None, conta_destino=None):
        self.tipo = tipo
        self.valor = valor
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.data_hora = datetime.now()

    def detalhes(self):
        if self.tipo == "transferencia":
            return f"{self.data_hora} - Transferência de {self.valor} de {self.conta_origem.numero} para {self.conta_destino.numero}"
        else:
            return f"{self.data_hora} - {self.tipo.capitalize()} de {self.valor} na conta {self.conta_origem.numero}"

def main():
    acoes = Acoes()
    
    while True:
        opcao = menu()
        if opcao == 1:
            numero = input("Digite o número da conta: ")
            titular = input("Digite o nome do titular: ")
            acoes.cadastrar_conta(numero, titular)
        elif opcao == 2:
            numero = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a ser sacado: "))
            acoes.sacar(numero, valor)
        elif opcao == 3:
            numero = input("Digite o número da conta: ")
            acoes.ver_extrato(numero)
        elif opcao == 4:
            numero = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a ser depositado: "))
            acoes.depositar(numero, valor)
        elif opcao == 5:
            numero_origem = input("Digite o número da conta de origem: ")
            numero_destino = input("Digite o número da conta de destino: ")
            valor = float(input("Digite o valor a ser transferido: "))
            acoes.transferir(numero_origem, numero_destino, valor)
            transacao = Transacao("transferencia", valor, conta_origem=acoes._buscar_conta(numero_origem), conta_destino=acoes._buscar_conta(numero_destino))
            print(transacao.detalhes())
        elif opcao == 6:
            numero = input("Digite o número da conta: ")

            modi = input("Deseja Mudar o Nome do Titular da Conta? s/n?")
            if modi.lower() == 's':
                novo_titular = input("Digite o novo nome do titular: ")
                acoes.modificar_nome_titular(numero, novo_titular)
            else:
                pass
        else:
            print("Opção inválida. Tente novamente.")


main()