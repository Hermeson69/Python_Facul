l1 = input('Lado1: ')
l2 = input('Lado2: ')
l3 = input('Lado3: ')

try:
    l1 = float(l1)
    l2 = float(l2)
    l3 = float(l3)
    
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        print('Os lados devem ser maiores que zero.')
    elif l1 >= (l2 + l3) or l2 >= (l1 + l3) or l3 >= (l1 + l2):
        print('Não é um triângulo')
    elif l1 == l2 == l3:
        print('Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Isósceles')
    else:
        print('Escaleno')
except ValueError:
    print('Por favor, insira um número válido.')
