def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def com(n,k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))

def arr(n, k):
    return fatorial(n) / fatorial(n-k)


def terceira():
    while True:
        print('1- Combinação')
        print('2 -Arranjo')
        print('Pressione qualquer numero para sair')
        op = int(input('Selecione: '))
        if op == 1:
            n = int(input('Digite um numero: '))
            k =  int(input('Digite um numero: '))
            if n < k: 
                print('N deve ser maior que K')
                continue

            c = com(n,k)
            print(c)

        elif op == 2:
            n = int(input('Digite um numero: '))
            k =  int(input('Digite um numero: '))
            if n < k: 
                print('N deve ser maior que K')
                continue

            a = arr(n,k)
            print(a)
        else:
            print('cabo')
            break

def main():
    terceira()

main()