
num = int(input("Digite um numero: "))

anterior =  num
estimativa = 1

while estimativa != anterior:
    anterior = estimativa
    estimativa = (estimativa + (num/estimativa))/2
    
print(estimativa)

# def achar_primo(num):
#     return all(num % i != 0 for i in range(2, num))

# num = int(input("Digite um numero: "))
# if achar_primo(num):
#     print("Numero primo")
# else:
#     print("Numero não primo")
def achar_primo(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Digite um numero: "))
if achar_primo(num):
    print("Numero primo")
else:
    print("Numero não primo")

def calcular_anos(X, Y):
    anos = 0
    while X <= Y:
        X = X + X * 0.03
        Y = Y + Y * 0.015
        anos += 1
    return anos

def valor_serie(n):
    soma = 0
    for i in range (1, n + 1):
        soma += i / (2* i -1)

    return soma

num = int(input("Digite um numero: "))
print(valor_serie(num))

def raiz_quadrada(numero):
    anterior = numero
    estimativa = 1

    while estimativa != anterior:
        anterior = estimativa
        estimativa = (estimativa + (numero / estimativa)) / 2
    
    return estimativa

def pitagoras(a, b):
    c_quadrado = (a * a) + (b * b) 
    return raiz_quadrada(c_quadrado)  

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = pitagoras(a, b)
print(f"O valor de c é: {c}")
