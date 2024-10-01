while True:
    try:
        x_i = float(input('Digite: '))
        y_i = float(input('Digite: '))

        if y_i != 0:
            z = x_i / y_i
            print(f'{x_i}/{y_i} = {z:.2f}')
            break
        elif y_i == 0:
            print('Divisão pro 0')
    except:
        print("Erro, digite novamente")