l1 = []
l2 = []
l3 = []

print("Primeira lista: ")
for i in range(10):
    lista = int(input(f"Digite o elemento na posição {i + 1}: "))
    l1.append(lista)

print("Segunda lista: ")
for i in range(10):
    lista = int(input(f"Digite o elemento na posição {i + 1}: "))
    l2.append(lista)

for i in range(10):
    l3.append(l1[i] * l2[i])

print("Terceira lista (multiplicação dos índices das duas primeiras listas): ")
print(l3)