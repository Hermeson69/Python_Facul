def main():
    custo_total = 200
    ingresso = 5.0
    quantidade_inicial = 120
    intervalo = 0.5
    aumento_vendas = 26

    lucro = []
    preco = []
    quantidade = []

    preco_inicial = ingresso

    while preco_inicial > 1.0:
        qnt_ingresso = quantidade_inicial + int((ingresso - preco_inicial) / intervalo) * aumento_vendas
        total = qnt_ingresso * preco_inicial
        lucro_atual = total - custo_total

        lucro.append(lucro_atual)
        preco.append(preco_inicial)
        quantidade.append(qnt_ingresso)

        preco_inicial -= intervalo


    print("Tabela de valores de lucros esperados:")
    print("Preço do Ingresso | Quantidade de Ingressos | Lucro")
    for i in range(len(lucro)):
        print(f"R$ {preco[i]:.2f}           | {quantidade[i]}                    | R$ {lucro[i]:.2f}")

    print("\nLucro máximo esperado:")
    print(f"Preço do ingresso: R$ {lucro.index(max(lucro)):.2f}")
    print(f"Quantidade de ingressos vendidos: {quantidade[lucro.index(max(lucro))]}")
    print(f"Lucro máximo: R$ {max(lucro):.2f}")

if __name__ == "__main__":
    main()