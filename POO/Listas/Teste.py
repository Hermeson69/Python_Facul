# lista = []

# while True: 
#     num = float(input('Novo numero para a lista (qualquer valor menor que 0 acaba): '))
#     if num < 0:
#         break   

#     lista.append(num)

# print(lista)
# print('Soma é: ' ,sum(lista))
# print('Media é: ', sum(lista)/len(lista))

# lista = [1,2,3,4,5,6,7]
# num = float(input('Busca: '))

# c = 0

# for i in lista:
#     if num == i:
#         c += 1

# print(c)
# lista = []

# while True:
#     num = float(input('Novo numero para a lista (qualquer valor menor que 0 acaba): '))
#     if num < 0:
#          break   

#     lista.append(num)
#     lista.sort()
#     print(lista)
#     lista.reverse()
#     print(lista)



num = int(input('Digite: '))

if num < 2:
     print('Não é primo')
else:
     primo = [x for x in range(2, (num // 2 + 1)) if num % x == 0]

     if primo:
          print('Não é primo')
     else:
          print('É primo')