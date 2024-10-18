def gerar_numeros_automatico(n=100):
    return list(range(1, n + 1))

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros.sort()
    n = len(numeros)
    if n % 2 == 0:
        return (numeros[n // 2 - 1] + numeros[n // 2]) / 2
    return numeros[n // 2]

def desvio_padrao(numeros):
    media = calcular_media(numeros)
    n = len(numeros)
    return (sum((x - media) ** 2 for x in numeros) / n) ** 0.5

def variancia(numeros):
    return desvio_padrao(numeros) ** 2

def main():
    numeros = gerar_numeros_automatico()
    print(f"Numeros gerados: {numeros}")
    print(f"Media: {calcular_media(numeros)}")
    print(f"Mediana: {calcular_mediana(numeros)}")
    print(f"Desvio padrão: {desvio_padrao(numeros)}")
    print(f"Variância: {variancia(numeros)}")

if __name__ == "__main__":
    main()
