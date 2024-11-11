class Conta():
    def __init__(self, Numero, titular, saldo):
        self.Numero = Numero
        self.titular = titular
        self.saldo = float(saldo)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Deposito feito com sucesso de {valor}')
        else: 
            print('Valor negativo')
            return
    def sacar(self, valor):
        if valor > self.saldo:
            print('NAO TEM DINHEIRO')
        else:
            self.saldo -= valor
    def extrato(self):
        print('Nome: {}| Saldo: {}| Numero: {}'.format(self.titular, self.saldo, self.Numero))




al = Conta(10092, 'marcos', 0.00)
al.extrato()
al.depositar(20000)
al.extrato()
al.sacar(30000)
al.extrato()