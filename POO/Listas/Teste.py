# lista = []

# while True: 
#     num = float(input('Novo numero para a lista (qualquer valor menor que 0 acaba): '))
#     if num < 0:
#         break   

#     lista.append(num)

# print(lista)
# print('Soma é: ' ,sum(lista))
# print('Media é: ', sum(lista)/len(lista))

lista = [1,2,3,4,5,6,7]
num = float(input('Busca: '))

c = 0

for i in lista:
    if num == i:
        c += 1

print(c)