def menu():
    print('1 - Mostrar frase.')
    print('2 - Mostrar frase Maiuscula.')
    print('3 - Mostrar frase Minuscula.')
    print('4 - Mostrar Primeira letra maiuscula frase.')
    print('5 - Escrever nova frase.')
    print('6 - Sair')
    op = int(input('Digite:'))
    return op


def main():
    frase = input('Digite a frase: ')

    while True:
        ops = menu()

        if ops == 1:
            print(frase)
        elif ops == 2:
            print(frase.upper())
        elif ops == 3:
            print(frase.lower())
        elif ops == 4:
            print(frase.capitalize())
        elif ops == 5:
            frase = input('Digite a frase: ')
        elif ops == 6:
            print('Fim')
            break
        else:
            print('Opção invalida')

main()