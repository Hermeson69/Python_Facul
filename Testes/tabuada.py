n = int(input('Numero: '))

i = int(input('Inicio: '))

f = int(input('fim: '))

for j in range(i, f + 1):
    r = n * j
    print(f'{n} x {j} = {r}')