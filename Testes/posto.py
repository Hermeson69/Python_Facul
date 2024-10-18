try:
    op = []
    print('G para gasolina')
    print ('A para Álcool')
    op = input('Qual é a sua escolha? ')

    qnt = 0

    qnt = float(input('quantos litros?: '))

    if op == 'G':
        if qnt <= 20:
            valor_f = qnt * 4.53 * 0.97  
        else:
            valor_f = qnt * 4.53 * 0.95  
    elif op == 'A':
        if qnt <= 20:
            valor_f = qnt * 3.45 * 0.96  
        else:
            valor_f = qnt * 3.45 * 0.94  
    else:
        raise ValueError("Opção inválida")

    print('O valor a ser pago é de R$ {:.2f}'.format(valor_f))


        
except:
    print("An error occurred")