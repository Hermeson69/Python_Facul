produtos = []

def adicionar_produto(produtos, nome, categoria, preco):
    produto = {
        'nome': nome.capitalize(),
        'preco': preco,
        'categoria': categoria.capitalize()
    }
    produtos.append(produto)

def listagem(produtos):
    if produtos:
        for idx, produto in enumerate(produtos, start=1):
            print(f"id= {idx} Nome: {produto['nome']}, Preço R$: {produto['preco']}, Categoria: {produto['categoria']}")
    else:
        print("Nenhum produto cadastrado!")

def cadastrar_produto(produtos):
    while True:
        op = input("Deseja cadastrar algum produto? s/n: ")
        if op.lower() == 's':
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            try:
                preco = float(input("Preço: "))
                adicionar_produto(produtos, nome.capitalize(), categoria.capitalize(), preco)
            except ValueError:
                print("Preço inválido. Digite um número.")
            break
        elif op.lower() == 'n':
            break

def busca(produtos):
    nome_busca = input('Nome do produto que deseja buscar: ')
    for produto in produtos:
        if produto['nome'] == nome_busca.capitalize():
            print(f"Nome: {produto['nome']}, Preço R$: {produto['preco']}, Categoria: {produto['categoria']}")
            return
    print("Produto não encontrado")

def excluir(produtos):
    nome_busca = input('Nome do produto que deseja excluir: ')
    for produto in produtos:
        if produto['nome'] == nome_busca:
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Categoria: {produto['categoria']}")
            produtos.remove(produto)
            print("Produto removido!")
            return
    print("Produto não encontrado")

def prod_por_categoria(pordutos):
    cont = 0
    cad_busca_quant = input('Quer saber a quantidade de qual categoria?:')
    for produto in produtos:
        if produto['categoria'] == cad_busca_quant.capitalize():
            cont+=1
    print(f'A categoria {cad_busca_quant} tem {cont} itens')
    print('Esses são:')
    listagem(produtos)


def menu():
    print('\n')
    print('Escolha uma opção: ')
    print('1 - Cadastro')
    print('2 - Busca')
    print('3 - Listagem')
    print('4 - Excluir')
    print('5 - Quantidade de Pordutos por categoria')
    print('6 - Sair')
    try:
        opcao = int(input('Digite a opção: '))
        return opcao
    except ValueError:
        print("Opção inválida. Digite um número.")
        return None

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar_produto(produtos)
        elif opcao == 2:
            busca(produtos)
        elif opcao == 3:
            listagem(produtos)
        elif opcao == 4:
            excluir(produtos)
        elif opcao == 5:
            prod_por_categoria(produtos)
        elif opcao == 6:
            break

main()
