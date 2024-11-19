from datetime import datetime as dt
import random as rd


def menu():
    print("1 - Cadastrar Pessoa")
    print("2 - Cadastrar Cartão")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Transferir")
    print("6 - Histórico de Transferências")
    print("7 - Estorno")
    print("8 - Mudar Nome Titular")
    print("9 - Imprimir Dados de uma Pessoa")
    op = int(input("Digite uma das opções acima: "))
    return op


# Classe usada para o cadastro de pessoas
class Pessoa:
    def __init__(self, nome, cpf, fone, endereco, idade):
        self._nome = nome
        self._cpf = cpf
        self._fone = fone
        self._endereco = endereco
        self._idade = idade
        self._cartoes = []

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, _):
        print("CPF não pode ser alterado!")

    @property
    def cartoes(self):
        return self._cartoes

    def adicionar_cartao(self, cartao):
        self._cartoes.append(cartao)
        cartao.pessoa = self


class Cartao:
    def __init__(self, pessoa=None):
        self._cvv = ''.join(str(rd.randint(0, 9)) for _ in range(3))
        self._numero = ''.join(str(rd.randint(0, 9)) for _ in range(16))
        self._data_limite = dt.now()
        self._pessoa = pessoa
        if pessoa:
            pessoa.adicionar_cartao(self)

    @property
    def cvv(self):
        return self._cvv

    @property
    def numero(self):
        return self._numero

    @property
    def data_limite(self):
        return self._data_limite

    @property
    def pessoa(self):
        return self._pessoa

    @pessoa.setter
    def pessoa(self, pessoa):
        self._pessoa = pessoa
        if pessoa and self not in pessoa.cartoes:
            pessoa.adicionar_cartao(self)


def imprimir_dados_pessoa(pessoa):
    """Exibe todas as informações da pessoa, incluindo os cartões associados."""
    print(f"Nome: {pessoa.nome}")
    print(f"CPF: {pessoa.cpf}")
    print(f"Telefone: {pessoa._fone}")
    print(f"Endereço: {pessoa._endereco}")
    print(f"Idade: {pessoa._idade}")
    print("Cartões:")
    for cartao in pessoa.cartoes:
        print(f"  Número: {cartao.numero}, CVV: {cartao.cvv}, Data Limite: {cartao.data_limite}")


def main():
    pessoas = {}

    while True:
        opcao = menu()
        if opcao == 1:
            # Cadastrar pessoa
            nome = input("Nome: ")
            cpf = input("CPF: ")
            fone = input("Telefone: ")
            endereco = input("Endereço: ")
            idade = int(input("Idade: "))
            pessoa = Pessoa(nome, cpf, fone, endereco, idade)
            pessoas[cpf] = pessoa
            print(f"Pessoa {nome} cadastrada com sucesso!")

        elif opcao == 2:
            # Cadastrar cartão
            cpf = input("Digite o CPF do titular: ")
            if cpf in pessoas:
                pessoa = pessoas[cpf]
                cartao = Cartao(pessoa=pessoa)
                print(f"Cartão cadastrado com sucesso! Número: {cartao.numero}, CVV: {cartao.cvv}")
            else:
                print("CPF não encontrado!")

        elif opcao == 8:
            # Alterar nome do titular
            cpf = input("Digite o CPF do titular: ")
            if cpf in pessoas:
                novo_nome = input("Digite o novo nome: ")
                pessoas[cpf]._nome = novo_nome
                print("Nome alterado com sucesso!")
            else:
                print("CPF não encontrado!")

        elif opcao == 9:
            # Imprimir dados de uma pessoa
            cpf = input("Digite o CPF da pessoa: ")
            if cpf in pessoas:
                imprimir_dados_pessoa(pessoas[cpf])
            else:
                print("CPF não encontrado!")

        else:
            print("Opção inválida!")



if __name__ == "__main__":
    main()
