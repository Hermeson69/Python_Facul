class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._dicionario = {}
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    def cad(self, nome, idade):
        self._dicionario[nome] = idade
    def imprimir(self):
        if self._dicionario:
            for nome, idade in self._dicionario.items():
                print(f"Nome: {nome}\nIdade: {idade}")
                print("----------------------")
        else:
            print("Nenhum usuário cadastrado.")
    def excluir(self, nome):
        if nome in self._dicionario:
            del self._dicionario[nome]
        else:
            print("Nome não cadastrado.")
    def busca(self, nome):
        if nome in self._dicionario:
            print(f"Nome: {nome}\nIdade: {self._dicionario[nome]}")
        else:
            print("Nome não cadastrado.")
def main():
    pessoas = Pessoa("Pessoas", 0)
    while True:
        opcao = int(input("1 - Cadastrar Pessoa\n2 - Exibir Todos\n3 - Excluir Pessoa\n4- buscar\n5 - Sair\n"))
        if opcao == 1:
            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))
            pessoas.cad(nome, idade)
        elif opcao == 2:
            pessoas.imprimir()
        elif opcao == 3:
            nome = input("Digite o nome da pessoa: ")
            pessoas.excluir(nome)
        elif opcao == 4:
            nome = input("Digite o nome da pessoa: ")
            pessoas.busca(nome)
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")
    pessoas.imprimir()

main()