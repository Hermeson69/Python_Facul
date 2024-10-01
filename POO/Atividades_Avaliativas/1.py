def primeira():
    while True:
        print('1-Triangulo')
        print('2-Quadrado')
        print('3-Circulo')
        print('4-Sair')
        op = int(input('Selecione: '))

        if op == 1:
            print('Informe os lados: ')
            l1 = float(input('Primeiro lado: '))
            l2 = float(input('Segundo lado: '))
            l3 = float(input('Terceiro lado: '))

            if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
                s = (l1 + l2 + l3) / 2
                area = (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5
                altura = (2 * area) / l1
                print('Altura:', altura)
            else:
                print('Os lados fornecidos não são válidos.')

        elif op == 2:
            print('Informe o lado do quadrado: ')
            lado = float(input('Lado: '))
            altura = lado  
            print('A altura do quadrado é:', altura)

        elif op == 3:
            print('Informe o raio do círculo: ')
            raio = float(input('Raio: '))
            altura = 2 * raio  
            print('A altura do círculo é:', altura)

        elif op == 4:
            print('Cabo')
            break

        else:
            print('Opção inválida.')



def main():
    primeira()
   
main()