def ispar(n):
    return n % 2 == 0 and n != 0

def impar_(n):
    return n % 2 != 0

def zero_(n):
    return n == 0

def main():
    lista = []
    while True:
        num = int(input('Numeros(digite qualquer numero menor que 0 para sair): '))
        if num < 0:
            break
        else:
            lista.append(num)

    par = list(filter(ispar, lista))
    impar = list(filter(impar_, lista))
    zero = list(filter(zero_, lista))

    par.sort()
    impar.sort()

    print(impar + zero + par)

main()