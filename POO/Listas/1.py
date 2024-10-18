lista = []
try:
    while True:
        num = int(input('Numeros(digite qualquer numero menor que 0 para sair): '))
        if num < 0:
            break
        elif num == 0:
            meio = len(lista) // 2
            lista.insert(meio, num)
        elif num % 2 == 0:
            lista.insert(0, num)
        elif num % 2 != 0:
            lista.append(num)
        else:
            print('Não é numero')
except ValueError:
    print('Erro: por favor, digite um número válido.')

print('Lista final:', lista)