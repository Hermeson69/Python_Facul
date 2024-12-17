import abc 
class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
    
    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")

    def __str__(self):
        return 'Numero: {}, Titular: {}, Saldo: {}, Limite: {}'.format(self._numero, self._titular, self._saldo, self._limite)

class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo
    def __str__(self):
       return 'CONTA CORRENTE: Numero: {}, Titular: {}, Saldo: {}, Limite: {}'.format(self._numero, self._titular, self._saldo, self._limite)

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo
    def __str__(self):
        return 'CONTA POUPANCA: Numero: {}, Titular: {}, Saldo: {}, Limite: {}'.format(self._numero, self._titular, self._saldo, self._limite)
    
class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
        return self._saldo
    def __str__(self):
        return 'CONTA INVESTIMENTO: Numero: {}, Titular: {}, Saldo: {}, Limite: {}'.format(self._numero, self._titular, self._saldo, self._limite)


if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'Joao', 1000, 2000)
    cp = ContaPoupanca('123-5', 'Jose', 1000, 2000)
    ci = ContaInvestimento('123-6', 'Maria', 1000, 2000)

    cc.atualiza(0.01)
    cp.atualiza(0.02)
    ci.atualiza(0.05)
    ci.deposita(1000)
    print(ci._saldo)

    print(cc._saldo)
    print(cp._saldo)
    print(ci._saldo)

    contas = [cc, cp, ci]
    for conta in contas:
        print(conta)