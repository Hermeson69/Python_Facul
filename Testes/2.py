# nome = input('Digite seu nome: ')

# if len(nome) > 10:
#     print(nome.upper())
# elif len(nome) < 10:
#     print(nome.lower())
# else:
#     print(nome.capitalize())

try:
    a = int(input('Digite a idade de A: '))
    b = int(input('Digite a idade de B: '))

    if a > b:
        print('A é maior que B')
    elif a == b:
        print('A e B têm a mesma idade')
    else:
        print('B é maior que A')
except ValueError:
    print('Por favor, insira um número válido.')