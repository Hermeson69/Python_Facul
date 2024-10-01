def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def segunda():
    while True:
        print('1- fatorial Normal')
        print('2 - fatorial com função')
        print('Pressione qualquer numero para sair')
        op = int(input('Selecione: '))
        if op == 1:
            num = int(input('Digite um numero: '))
            f = 1
            for i in range(1, num + 1):
                f *= i
            print(f)
        elif op == 2:
            num = int(input('Digite um numero: '))
            print(fatorial(num))
        else:
            print('cabo')
            break

def main():
    segunda()

main()