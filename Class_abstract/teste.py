from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, CPF, salario):
        self._nome = nome
        self._CPF = CPF
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def CPF(self):
        return self._CPF

    @property
    def salario(self):
        return self._salario

    @abstractmethod
    def get_bonificacao(self):
        pass
    
    def __str__(self):
        return 'Nome: {}, CPF: {}, Salario: {}'.format(self._nome, self._CPF, self._salario)

class Gerente(Funcionario):
    def __init__(self, nome, CPF, salario, senha, qtd_funcionarios):
        super().__init__(nome, CPF, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    @property
    def senha(self):
        return self._senha

    @property
    def qtd_funcionarios(self):
        return self._qtd_funcionarios

    def autentica(self, senha):
        if self._senha == senha:
            print('Acesso permitido')
            return True
        else:
            print('Acesso negado')
            return False

    def get_bonificacao(self):
        return self._salario * 0.4 + 2000

    def __str__(self):
        return 'Nome: {}, CPF: {}, Salario: {}, Senha: {}, Qtd Funcionarios: {}'.format(self._nome, self._CPF, self._salario, self._senha, self._qtd_funcionarios)

class Atendente(Funcionario):
    def get_bonificacao(self):
        return self._salario * 0.4 + 2000

    def __str__(self):
        return 'Nome: {}, CPF: {}, Salario: {}'.format(self._nome, self._CPF, self._salario)

class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, funcionario):
        bonificacao = funcionario.get_bonificacao()
        print(f'Bonificação de {funcionario.nome}: {bonificacao}')
        funcionario._salario += bonificacao
        self._total_bonificacoes += bonificacao

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

if __name__ == "__main__":
    gerente = Gerente('Joao', '123.456.789-00', 5000, '1234', 10)
    atendente = Atendente('Maria', '987.654.321-00', 2000)
    atendente2 = Atendente('Paula', '987.654.321-00', 2200)

    controle = ControleDeBonificacoes()
    funcionarios = [gerente, atendente, atendente2]
    for funcionario in funcionarios:
        controle.registra(funcionario)
        print(funcionario)

    print('Total de bonificações: {}'.format(controle.total_bonificacoes))
