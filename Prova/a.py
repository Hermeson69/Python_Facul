num = int(input("Digite um numero: "))

anterior =  num
estimativa = 1

while estimativa != anterior:
    anterior = estimativa
    estimativa = (estimativa + (num/estimativa))/2
    
print(estimativa)