import abc

class Pessoa(abc.ABC):
    def __init__(self, id, nome, sexo, idade, tipo_sangue):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        self._tipo = tipo_sangue
    @abc.abstractmethod
    def id(self):
        return self._id
    @property
    def nome(self):
        return self._nome
    @property
    def sexo(self):
        return self._sexo
    @property
    def idade(self):
        return self._idade
    @property
    def tipo_sangue(self):
        return self._tipo

class Autenticavel(abc.ABC):
    @abc.abstractmethod
    def autentica(self, senha):
        pass

class Funcionario(Pessoa, Autenticavel):
    def __init__(self, id, nome, sexo, idade, tipo_sangue, cargo, salario, senha):
        super().__init__(id, nome, sexo, idade, tipo_sangue)
        self._cargo = cargo
        self._salario = salario
        self._senha = senha

    def autentica(self, senha):
        return self._senha == senha

    @property
    def salario(self):
        return self._salario

    def __str__(self):
        return 'ID: {}, Nome: {}, Sexo: {}, Idade: {}, Tipo Sanguineo: {}, Salario: {}'.format(self._id, self._nome, self._sexo, self._idade, self._tipo, self._salario)