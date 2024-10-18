def soma():
    a + b
    return a + b

def sub():
    a - b
    return a - b

def mult():
    a * b
    return a * b

def div():
    a/b
    if b == 0:
        return "Não é possível dividir por zero"
    return a + b

def menu():
    print('1 - soma')
    print('2 - subtracao')
    print('3 - multiplicacao')
    print('4 - divisao')
    print('5 - sair')
    opc = int(input('selecione: '))

    return opc

ocp = menu()
if ocp == 1:
    a = float(input('digite o primeiro valor: '))
    b = float(input('digite o segundo valor: '))
    print(soma())
elif ocp == 2:
    a = float(input('digite o primeiro valor: '))
    b = float(input('digite o segundo valor: '))
    print(sub())
elif ocp == 3:
    a = float(input('digite o primeiro valor: '))
    b = float(input('digite o segundo valor: '))
    print(mult())
elif ocp == 4:
    a = float(input('digite o primeiro valor: '))
    b = float(input('digite o segundo valor: '))
    print(div())
else:
    print('saindo...')