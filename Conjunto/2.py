dicionario = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Peru': 'Lima',
    'Colômbia': 'Bogotá',
    'Uruguai': 'Montevidéu',
    'Paraguai': 'Assunção',
    'Bolívia': 'Sucre',
    'Equador': 'Quito',
    'Venezuela': 'Caracas'
}

pais = input("Digite o nome do pais: ")

for chave in dicionario.keys():

    if pais in chave:
        print(dicionario[pais])
        break
    else:
        print("Pais não encontrado")
        break