import random as rand

# Fazer todo slide 3;
# Raiz quadrada:
'''
'''
# Lista:
'''
strinig = input("Digite: ")
cont = 0

for i in strinig:
    cont+=1

print(f"A string {strinig}, tem {cont} elementos")


#LISTA DENTRO DE LISTA
def lista_dentro_lista(lst):
    for elements in lst:
        if isinstance(elements, list):
            print(elements)
        else:
            print(elements)

#Busca elemento lista          
string = input('Digite: ')
cont = 0
busca = input("Busque: ")
for i in string:
    cont += 1
    if i == busca:
        print(f"Elemento {busca} encontrado na(s) posicoes: {cont}")

a = 'Flavio'
b = list(a)
for i in range(len(b)):
    for j in range(0, len(b)-i-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
c = ''.join(b)
print(c)

num = rand.randint(1, 100)

while True:
    cont= 0
    busca = int(input("Digite: "))
    if busca == num:
        print("Parabens")
        break
    else:
        print('Elemento não encontrado')
        cont +=1
        if cont == 10:
            print('Deu merda')
            break 
        
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(lista)//2):
    lista[i], lista[len(lista) - i - 1] = lista[len(lista) - i - 1], lista[i]
print(lista)
'''
# def ler_tempos():
#     corredores = {}
#     for _ in range(5):
#         nome = input("Digite o nome do corredor: ")
#         tempo = []
#         for i in range(3):
#             tempo.append(float(input(f"Digite o tempo do {i + 1}º percurso: ")))
#         corredores[nome] = tempo
#     return corredores

# corredores = ler_tempos()
# for nome, tempos in corredores.items():
#     media = sum(tempos) / len(tempos)
#     print(f"Corredor: {nome}, Tempos: {tempos}, Média: {media:.2f}")

# def ler_tempos2():
#     alunos = {}
#     qnt = int(input("Quantidade de alunos: "))
#     for _ in range(qnt):
#         nome = input('Nome: ')
#         notas = []
#         for i in range(3):
#             notas.append(float(input(f'Digite a nota {i + 1}: ')))
#         alunos[nome] = notas
#     return alunos

# alunos = ler_tempos2()
# for nome, notas in alunos.items():
#     media = sum(notas)/len(notas)
#     print(f"Aluno: {nome}, notas: {notas}, media: {media:.2f}")





# num = int(input("Digite um numero: "))

# j =  num
# k = 1

# while k != j:
#     j = k
#     k = (k + (num/k))/2
    
# print(k)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lista = [1, 2, 3, 5, 7, 9, 11, 13]

for num in lista:
    if is_prime(num):
        print(f"{num} é primo")
        
