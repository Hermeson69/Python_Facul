def ler_tempos():
    corredores = {}
    for _ in range(5):
        nome = input("Digite o nome do corredor: ")
        tempo = []
        for i in range(3):
            tempo.append(float(input(f"Digite o tempo do {i + 1}º percurso: ")))
        corredores[nome] = tempo
    return corredores

def melhor_tempo(corredores):
    melhor = float('Inf')
    melhor_corredor = None
    for corredor in corredores:
        tempo = sum(corredores[corredor])
        if tempo < melhor:
            melhor = tempo
            melhor_corredor = corredor
    return melhor_corredor, melhor

def main():
    corredores = ler_tempos()
    melhor_corredor, tempo_total = melhor_tempo(corredores)
    print(f"O melhor corredor é {melhor_corredor} com o tempo total de {tempo_total:.2f} segundos.")

main()
