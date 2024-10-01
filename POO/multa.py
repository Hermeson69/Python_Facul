try:
    peso = float(input('Digite o Peso do Peixe: '))

    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        print(f'Excesso de peso: {excesso:.2f} e Multa: {multa:.2f}')
    else:
        print('Excesso de peso: 0.0 e Multa: 0.0')

        
except:
    print("An error occurred")