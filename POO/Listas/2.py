import random

lista = []
try:
    while True:
        i = int(input('Inicio: '))
        f = int(input('Fim: '))
        if i > f:
            print("O valor de 'Inicio' deve ser menor ou igual ao valor de 'Fim'. Tente novamente.")
            continue
        quantidade = int(input('Quantos números deseja gerar? '))
        for _ in range(quantidade):
            x = random.randint(i, f)
            lista.append(x)
            print(f"Número aleatório gerado: {x}")
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break
except ValueError:
    print("Por favor, insira um número válido.")

print("Lista de números gerados:", lista)