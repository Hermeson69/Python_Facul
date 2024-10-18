def adicionar_nome(agenda, nome, telefones):
    agenda[nome] = telefones

def adicionar_telefone(agenda, nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        print("Nome não encontrado na agenda")

def excluir_telefone(agenda, nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            if not agenda[nome]: 
                del agenda[nome]
        else:
            print("Telefone não encontrado")
    else:
        print("Nome não encontrado na agenda")

def excluir_nome(agenda, nome):
    if nome in agenda:
        del agenda[nome]
    else:
        print("Nome não encontrado na agenda")

def consultar_telefone(agenda, nome):
    if nome in agenda:
        return agenda[nome]
    else:
        print("Nome não encontrado na agenda")
        return None

def main():
    agenda = {}
    while True:
        print("1 - Novo Nome")
        print("2 - Novo Telefone")
        print("3 - Excluir Telefone")
        print("4 - Excluir Nome")
        print("5 - Consultar telefone")
        print("6 - Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            telefones = input("Digite os telefones separados por vírgula: ").split(',')
            adicionar_nome(agenda, nome, telefones)
        elif opcao == '2':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            adicionar_telefone(agenda, nome, telefone)
        elif opcao == '3':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            excluir_telefone(agenda, nome, telefone)
        elif opcao == '4':
            nome = input("Digite o nome: ")
            excluir_nome(agenda, nome)
        elif opcao == '5':
            nome = input("Digite o nome: ")
            telefones = consultar_telefone(agenda, nome)
            if telefones:
                print(f"Telefones de {nome}: {', '.join(telefones)}")
        elif opcao == '6':
            break
        else:
            print("Opção inválida, tente novamente.")


main()