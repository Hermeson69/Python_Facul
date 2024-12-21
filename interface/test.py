import abc

class Autenticavel(abc.ABC):
    @abc.abstractmethod
    def autentica(self, senha):
        pass

class Cliente(Autenticavel):
    def __init__(self, nome, cpf, senha):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha

    def autentica(self, senha):
        return self._senha == senha

    def __str__(self):
        return 'Nome: {}, CPF: {}'.format(self._nome, self._cpf)

class Funcionario(Autenticavel):
    def __init__(self, nome, cpf, salario, senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha

    def autentica(self, senha):
        return self._senha == senha

    def __str__(self):
        return 'Nome: {}, CPF: {}, Salario: {}'.format(self._nome, self._cpf, self._salario)

if __name__ == '__main__':
    cliente = Cliente('João', '123.456.789-00', '111111')
    funcionario = Funcionario('Maria', '987.654.321-00', 5000, 'senha_funcionario')
    
    print(cliente)
    print('Autenticação cliente:', cliente.autentica('111111'))
    
    
    print(funcionario)
    print('Autenticação funcionário:', funcionario.autentica('senha_funcionario'))
