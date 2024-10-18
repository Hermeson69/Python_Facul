# Função para ler os dados de uma pessoa
def ler_dados():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    cep = input("CEP: ")
    bairro = input("Bairro: ")
    telefone = input("Telefone: ")
    return {'nome': nome, 'endereco': endereco, 'cep': cep, 'bairro': bairro, 'telefone': telefone}

agenda = []

for i in range(10):
    print(f"Digite os dados da pessoa {i + 1}:")
    pessoa = ler_dados()
    agenda.append(pessoa)

print("\nAgenda em ordem invertida:")
for pessoa in reversed(agenda):
    print(pessoa)
