class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print('Saldo insuficiente')

    def atualizar(self, taxa):
        self._saldo += self._saldo * taxa

    def __str__(self):
        return 'Titular: {}, Numero da Conta {}, Saldo: {}'.format(self._titular,self._numero, self._saldo)

class ContaCorrente(Conta):
    def atualizar(self, taxa):
        super().atualizar(taxa * 2)

    def depositar(self, valor):
        super().depositar(valor - 0.10)

class ContaPoupanca(Conta):
    def atualizar(self, taxa):
        super().atualizar(taxa * 3)

class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def selic(self):
        return self._selic

    @selic.setter
    def selic(self, selic):
        self._selic = selic

    @property
    def saldo_total(self):
        return self._saldo_total

    @saldo_total.setter
    def saldo_total(self, saldo_total):
        self._saldo_total = saldo_total

    def roda(self, contas):
        for conta in contas:
            print('Saldo da conta: {}'.format(conta.saldo))
            conta.atualizar(self._selic)
            self._saldo_total += conta.saldo
            print("Saldo Final: {}".format(self._saldo_total))

if __name__ == '__main__':
    cc = ContaCorrente('João', '11-33', 1000)
    cp = ContaPoupanca('Maria', '11-23',1000)
    
    contas = [cc, cp]
    a = AtualizadorDeContas(0.01)
    a.roda(contas)

  
    

    cc.depositar(100)
    cp.depositar(100)

    cc.sacar(100)
    cp.sacar(100)

    cc.atualizar(0.01)
    cp.atualizar(0.01)

    print(cc)
    print(cp)