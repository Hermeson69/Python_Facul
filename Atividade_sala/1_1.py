def adicionar_produto(produtos, nome, categoria, preco):
    produtos[nome] = {'categoria': categoria, 'preco': preco}

def listagem(produtos):
    if produtos:
        for nome, detalhes in produtos.items():
            print(f"Nome: {nome}, Preço: {detalhes['preco']}, Categoria: {detalhes['categoria']}")
    else:
        print("Nenhum produto cadastrado!")
        op = input("Deseja cadastrar algum produto? (s/n): ")
        if op.lower() == 's':
            adicionar_produto(produtos, input("Nome: "), input("Categoria: "), float(input("Preço: ")))

def busca(produtos):
    nome_busca = input('Nome do produto que deseja buscar: ')
    if nome_busca in produtos:
        detalhes = produtos[nome_busca]
        print(f"Nome: {nome_busca}, Preço: {detalhes['preco']}, Categoria: {detalhes['categoria']}")
    else:
        print("Produto não encontrado")

def excluir(produtos):
    nome_busca = input('Nome do produto que deseja excluir: ')
    if nome_busca in produtos:
        del produtos[nome_busca]
        print(f"Produto {nome_busca} removido com sucesso.")
    else:
        print("Produto não encontrado")

def menu():
    print('\nEscolha uma opção: ')
    print('1 - Cadastro')
    print('2 - Busca')
    print('3 - Listagem')
    print('4 - Excluir')
    print('5 - Sair')
    opcao = int(input('Digite a opção: '))
    return opcao

def main():
    produtos = {}

    while True:
        opcao = menu()
        if opcao == 1:
            adicionar_produto(produtos, input("Nome: "), input("Categoria: "), float(input("Preço: ")))
        elif opcao == 2:
            busca(produtos)
        elif opcao == 3:
            listagem(produtos)
        elif opcao == 4:
            excluir(produtos)
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()