import functools as ft

numeros = [1, 2, 3, 4, 5, 6]

pares= filter(lambda x: x%2==0, numeros)
dobro = map(lambda x: x*2, numeros)
soma = ft.reduce(lambda x, y: x+y, numeros)


print(list(pares))

print(list(dobro))

print(soma)

