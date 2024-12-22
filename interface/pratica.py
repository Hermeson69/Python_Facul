# Treino Interfece
# 2020-11-10
import abc

class Tributavel(abc.ABC):
    @abc.abstractmethod
    def get_valor_imposto(self):
        pass

class Conta():
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        self._saldo -= valor

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self._saldo, self._titular))

    def get_saldo(self):
        return self._saldo

    def get_titular(self):
        return self._titular

    def get_numero(self):
        return self._numero

    def get_valor_imposto(self):
        return self._saldo * 0.01

class help(Tributavel):
    def documentoção(self):
        return 'Ajuda'
    
class ContaCorrente(Conta, Tributavel):
    def get_valor_imposto(self):
        return super().get_valor_imposto() * 0.10

class SeguroDeVida(Tributavel):
    def __init__ (self, valor, titular, num_apolice):
        self._valor = valor
        self._titular = titular
        self._num_apolice = num_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

class ManipuladorDeTributaveis():
    def calcular_impostos(self, lista_tributavel):
        total = 0
        for i in lista_tributavel:
            if (isinstance(i, Tributavel)):
                total += i.get_valor_imposto()
            else: 
                print(i.__repr__(), "não é tributavel")
        return total

class ContaInvestimento(Conta, Tributavel):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
    def get_valor_imposto(self):
        return self._saldo * 0.03

if __name__ == "__main__":
    conta1 = ContaCorrente('123-4', 'João', 1000.0, 5000.0)
    conta2 = ContaCorrente('123-5', 'Maria', 2000.0, 4000.0)
    seguro1 = SeguroDeVida(100000.0, 'José', '345-77')
    conta_investimento = ContaInvestimento('123-6', 'Ana', 3000.0, 6000.0)
    
    lista_tributaveis = [conta1, conta2, seguro1, conta_investimento]
    
    manipulador = ManipuladorDeTributaveis()
    total_impostos = manipulador.calcular_impostos(lista_tributaveis)
    
    for item in lista_tributaveis:
        if isinstance(item, Conta):
            print(f'Conta: {item.get_numero()}, Titular: {item.get_titular()}, Saldo: {item.get_saldo()}, Imposto: {item.get_valor_imposto()}')
        elif isinstance(item, SeguroDeVida):
            print(f'Seguro de Vida: Apólice: {item._num_apolice}, Titular: {item._titular}, Valor: {item._valor}, Imposto: {item.get_valor_imposto()}')
    
    print(f'Total de impostos: {total_impostos}')