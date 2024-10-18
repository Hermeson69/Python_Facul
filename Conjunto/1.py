# turma1 = ['flavio', 'joao', 'maria', 'pedro']
# turma2 = ['ana', 'julia', 'flavio', 'pedro']

# print(f'tuma 1 {turma1}')
# print(f'tuma 2 {turma2}')

# turma1.remove('joao')

# print(f'alunos nas 2 tumas: {set(turma1) & set(turma2)}')
# print(f'alunos na 1° tumas: {set(turma1) - set(turma2)}')

dicionario = {
    'nome':  'flavio',
    'idade':  20,
    'cidade': 'sao paulo',
}

dicionario['cep'] = '88283-992'
dicionario['sexo'] = '3 vez por hora'

print(dicionario)

print(dicionario.keys)

dicionario2 = {}

dicionario2 = dicionario.copy()

print(dicionario2)



print(dicionario2.get('nome'))
