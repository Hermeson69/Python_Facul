def main():
    binario = ''
    decimal = int(input('Digite um decimal: '))
    if decimal == 0:
        binario = '0'
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    print(binario)

main()