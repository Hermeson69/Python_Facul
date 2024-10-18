def lista():
    return [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

def menor(lst):
    menor = lst[0]
    for num in lst:
        if num < menor:
            menor = num
    print(menor)

def maior(lst):
    maior = lst[0]
    for num in lst:
        if num > maior:
            maior = num
    print(maior)

def media(lst):
    media = sum(lst) / len(lst)
    print(media)

def ocorrencia(lst):
    cont = 0
    for num in lst:
        if num == lst[0]:
            cont += 1
    print(cont)

def soma_negativos(lst):
    soma_nega = 0
    for num in lst:
        if num < 0:
            soma_nega += num
    print(soma_nega)

def menu():
    while True:
        print('---------------------------')
        print('1 - Mostrar a lista')
        print('2 - Mostrar o menor valor')
        print('3 - Mostrar o maior valor')
        print('4 - Mostrar a média dos valores')
        print('5 - Ocorrencia do 1 numero da lista')
        print('6 - Soma dos negativos da lista')
        opcao = int(input('Digite sua escolha ou qualquer outro para sair: '))

        if opcao < 1 or opcao > 6:
            print('Opção invalida')
            continue

        lst = lista()
        if opcao == 1:
            print(lst)
        elif opcao == 2:
            menor(lst)
        elif opcao == 3:
            maior(lst)
        elif opcao == 4:
            media(lst)
        elif opcao == 5:
            ocorrencia(lst)
        elif opcao == 6:
            soma_negativos(lst)
        else:
            print('Fim do programa')
            break

def main():
    menu()

main()
