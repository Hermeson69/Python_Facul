def valor(n):
    s = 0

    for i in range(1, n + 1):
        s += i / (2 * i - 1)
    return s

if __name__ == "__main__":
    n = int(input("Digite um número inteiro: "))
    resultado = valor(n)
    print(f"O resultado é: {resultado}")