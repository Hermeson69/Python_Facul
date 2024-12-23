from datetime import datetime

def menu():
    print("1 - Depositar Dinheiro\n")
    print("2 - Sacar Dinheiro\n")
    print("3 - Ver Extrato\n")
    print("4 - Criar Conta\n")
    print("5 - Transferir\n")
    print("6 - Sair\n")
    op = int(input("Digite uma Opção: \n"))
    return op

class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")

    def transferir(self, conta_destino, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de {valor} realizada com sucesso.")

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo: {self.saldo} | Número: {self.numero}")

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
    contas = {}
    transacoes = []
    op = menu()

    while op != 6:
        if op == 1:
            numero = input("Digite o número da conta para depósito: ")
            if numero in contas:
                valor = float(input("Digite o valor a ser depositado: "))
                contas[numero].depositar(valor)
                transacoes.append(Transacao("deposito", valor, conta_origem=contas[numero]))
            else:
                print("Conta não encontrada.")

        elif op == 2:
            numero = input("Digite o número da conta para saque: ")
            if numero in contas:
                valor = float(input("Digite o valor a ser sacado: "))
                contas[numero].sacar(valor)
                transacoes.append(Transacao("saque", valor, conta_origem=contas[numero]))
            else:
                print("Conta não encontrada.")

        elif op == 3:
            numero = input("Digite o número da conta para ver extrato: ")
            if numero in contas:
                contas[numero].extrato()
            else:
                print("Conta não encontrada.")

        elif op == 4:
            numero = input("Digite o número da nova conta: ")
            titular = input("Digite o nome do titular: ")
            saldo = float(input("Digite o saldo inicial: "))
            contas[numero] = Conta(numero, titular, saldo)
            print("Conta criada com sucesso.")

        elif op == 5:
            numero_origem = input("Digite o número da conta de origem: ")
            numero_destino = input("Digite o número da conta de destino: ")
            if numero_origem in contas and numero_destino in contas:
                valor = float(input("Digite o valor a ser transferido: "))
                contas[numero_origem].transferir(contas[numero_destino], valor)
                transacoes.append(Transacao("transferencia", valor, conta_origem=contas[numero_origem], conta_destino=contas[numero_destino]))
            else:
                print("Conta de origem ou destino não encontrada.")

        else:
            print("Opção inválida.")

        op = menu()

    for transacao in transacoes:
        print(transacao.detalhes())

main()