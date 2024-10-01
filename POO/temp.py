try:

    F = float(input('Temperatura em Farenheit: '))
    C = (F - 32) * 5/9
    print(f'{F} Farenheit é igual a {C} Celsius')

except:
    print("An error")