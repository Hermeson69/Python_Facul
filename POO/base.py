try:
    base = float(input('Base: '))
    expoente = int(input('Expoente: '))  
    valor = 1  

    for i in range(expoente):
        valor *= base  

  
    print(f'{base} elevado a {expoente} é {valor}')
except ValueError:
    print('Erro: Por favor, insira um valor numérico para base e expoente')