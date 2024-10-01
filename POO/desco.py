try:
    salario = float(input('Digite o Salario: '))
    print(f'{salario:.2f}')

    inss = (salario * 0.08)
    ir = (salario * 0.11)
    sinicato = (salario * 0.005)

    salario_liquido = salario - inss - ir - sinicato
    valor_desconto = inss + ir + sinicato

    print(f'Salario Liquido e Valor Desconto: {salario_liquido:.2f} e Valor Descontado: {valor_desconto:.2f}')  
        
except:
    print("An error occurred")