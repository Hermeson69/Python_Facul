class Conta():
    def __init__(self, titular, numero):
        self._titular = titular  # _ na frente do atributo quer dizer Privado
        self._numero = numero
        self._saldo = 0

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, novo_titular):
        modi = input('Deseja mudar seu nome titular s/n? \n')

        if modi.lower() == 's':
            novo_titular = input('Digite o novo nome do titular: ')
            self._titular = novo_titular
        elif modi.lower() == 'n':
            pass

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, _):
        print("Erro: Número da conta não pode ser alterado!")

    @property  # Get (retorno)
    def saldo(self):
        return self._saldo

    @saldo.setter  # Set(altera)
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo\n')
        else:
            self._saldo = saldo
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

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo: {self.saldo} | Número: {self.numero}")

c1 = Conta('flavio', '12344')
c1.numero = '222'
c1.saldo = 1000
print(c1.numero)
print(c1.saldo)

# Para testar a mudança do titular
c1.titular = 'novo_nome'
c1.extrato()  
c1.depositar(100)
c1.sacar(10)
print(c1.titular)
c1.extrato()