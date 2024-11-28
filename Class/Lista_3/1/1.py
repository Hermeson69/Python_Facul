from datetime import datetime as dt
class Pessoa:
    def __init__(self, data_nascimeto, nome, altura):
        self._nome = nome
        self._data_nascimento = data_nascimeto
        self._altura = altura
    @property
    def nome (self):
        return self._nome
    @property
    def data_nascimento(self):
        return self._data_nascimento
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            print("Altura inválida.")
    @property
    def idade(self):
        return dt.now().year - self._data_nascimento.year

def main():
    pessoas = {
    }

    while True:
        opcao = int(input("1 - Cadastrar Pessoa\n2 - Exibir dados de uma pessoa\n3 - Sair\n"))
        if opcao == 1:
            nome = input("Digite o nome da pessoa: ")
            data_nascimento = input("Digite a data de nascimento da pessoa (dd/mm/aaaa): ")
            altura = float(input("Digite a altura da pessoa: "))
            data_nascimento = dt.strptime(data_nascimento, "%d/%m/%Y")
            pessoa = Pessoa(data_nascimento, nome, altura)
            pessoas[nome] = pessoa
        elif opcao == 2:
            nome = input("Digite o nome da pessoa: ")
            if nome in pessoas:
                pessoa = pessoas[nome]
                print(f"Nome: {pessoa.nome}\nData de Nascimento: {pessoa.data_nascimento}\nAltura: {pessoa.altura}\nIdade: {pessoa.idade}")
            else:
                print("Pessoa não cadastrada.")
        elif opcao == 3:
            break
        else:
            print("Opção inválida. Tente novamente.")

main()