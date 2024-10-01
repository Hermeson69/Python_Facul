import pandas as pd

def menu():
    while True:
        print('\n')
        print('Escolha uma opção: ')
        print('1 - Cadastro')
        print('2 - Busca')
        print('3 - Editar')
        print('4 - Excluir')
        print('5 - Exportar')
        print('6 - Sair')
        opcao = int(input('Digite a opção: '))
        return opcao

def cadastro(usuarios):
    while True:
        print('Cadastro de Usuário')
        nome = input('Digite o Nome: ')
        idade = input('Digite a Idade: ')
        salario = input('Digite o Salario: ')
        sexo = input('Digite o Sexo (f/m): ')
        estado_civil = input('Digite o Estado Civil (s/c/v/d): ')
        if not estado_civil:
            estado_civil = 's'

        sexo_dict = {
            'f': 'Feminino',
            'm': 'Masculino'
        }

        estado_dict = {
            's': 'Solteiro',
            'c': 'Casado',
            'v': 'Viúvo',
            'd': 'Divorciado'
        }

        usuario = {
            'nome': nome,
            'idade': idade,
            'salario': salario,
            'sexo': sexo_dict[sexo],
            'estado_civil': estado_dict[estado_civil]
        }

        usuarios.append(usuario)
        print(f'\n Nome: {nome}\nIdade: {idade}\nSalario: {salario}\nSexo: {sexo_dict[sexo]}\nEstado Civil: {estado_dict[estado_civil]}')

        continuar = input('Deseja cadastrar outro usuário? (s/n): ')
        if continuar.lower() != 's':
            break
    return usuarios

def busca(usuarios):
    print('\n')
    print('Escolha uma opção para busca: ')
    print('1 - Nome')
    print('2 - Idade')
    print('3 - Salario')
    print('4 - Sexo')
    print('5 - Estado Civil')
    print('6 - Sair')
    opcao = int(input('Digite a opção: '))

    if opcao == 1:
        nome = input('Digite o Nome: ')
        for usuario in usuarios:
            if usuario['nome'] == nome:
                print(usuario)
    elif opcao == 2:
        idade = input('Digite a Idade: ')
        for usuario in usuarios:
            if usuario['idade'] == idade:
                print(usuario)
    elif opcao == 3:
        salario = input('Digite o Salario: ')
        for usuario in usuarios:
            if usuario['salario'] == salario:
                print(usuario)
    elif opcao == 4:
        sexo = input('Digite o Sexo (f/m): ')
        for usuario in usuarios:
            if usuario['sexo'] == sexo:
                print(usuario)
    elif opcao == 5:
        estado_civil = input('Digite o Estado Civil (Solteiro/Casado/Viúvo/Divorciado): ')
        for usuario in usuarios:
            if usuario['estado_civil'] == estado_civil:
                print(usuario)

def alterar(usuarios):
    busca_usuario = input('Nome do Usuário a mudar os dados: \n')
    for usuario in usuarios:
        if usuario['nome'] == busca_usuario:
            usuario_encontrado = usuario
            print(f'\nNome: {usuario_encontrado["nome"]}\nIdade: {usuario_encontrado["idade"]}\nSalario: {usuario_encontrado["salario"]}\nSexo: {usuario_encontrado["sexo"]}\nEstado Civil: {usuario_encontrado["estado_civil"]}')
            break
    print('\nEscolha uma opção para alteração: ')
    print('1 - Nome')
    print('2 - Idade')
    print('3 - Salario')
    print('4 - Sexo')
    print('5 - Estado Civil')
    print('6 - Sair')
    opcao2 = int(input('Digite a opção: '))

    if opcao2 == 1:
        novo_nome = input('Digite o novo Nome: ')
        usuario_encontrado['nome'] = novo_nome
        print('Nome alterado com sucesso!')
    elif opcao2 == 2:
        nova_idade = input('Digite a nova Idade: ')
        usuario_encontrado['idade'] = nova_idade
        print('Idade alterada com sucesso!')
    elif opcao2 == 3:
        novo_salario = input('Digite o novo Salario: ')
        usuario_encontrado['salario'] = novo_salario
        print('Salario alterado com sucesso!')
    elif opcao2 == 4:
        novo_sexo = input('Digite o novo Sexo (f/m): ')
        sexo_dict = {
            'f': 'Feminino',
            'm': 'Masculino'
        }
        usuario_encontrado['sexo'] = sexo_dict[novo_sexo]
        print('Sexo alterado com sucesso!')
    elif opcao2 == 5:
        novo_estado_civil = input('Digite o novo Estado Civil (s/c/v/d): ')
        estado_dict = {
            's': 'Solteiro',
            'c': 'Casado',
            'v': 'Viúvo',
            'd': 'Divorciado'
        }
        usuario_encontrado['estado_civil'] = estado_dict[novo_estado_civil]
        print('Estado Civil alterado com sucesso!')
    elif opcao2 == 6:
        return
    
def excluir(usuarios):
    busca_usuario = input('Nome do Usuário a mudar os dados: \n')
    for usuario in usuarios:
        if usuario['nome'] == busca_usuario:
            usuario_encontrado = usuario
            print(f'\nNome: {usuario_encontrado["nome"]}\nIdade: {usuario_encontrado["idade"]}\nSalario: {usuario_encontrado["salario"]}\nSexo: {usuario_encontrado["sexo"]}\nEstado Civil: {usuario_encontrado["estado_civil"]}')
            usuarios.remove(usuario_encontrado)
            break
        return

def main():
    usuarios = []
    while True:
        opcao = menu()
        if opcao == 1:
            usuarios = cadastro(usuarios)
        elif opcao == 2:
            busca(usuarios)
        elif opcao == 3:
            alterar(usuarios)
        elif opcao == 4:
            excluir(usuarios)
        elif opcao == 6:
            break

if __name__ == "__main__":
    main()