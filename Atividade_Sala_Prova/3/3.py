def calcular_anos(X, Y):
    A = 0.03
    B = 0.015
    anos = 0
    
    while X <= Y:
        X += X * A
        Y += Y * B
        anos += 1
    
    return anos

if __name__ == "__main__":
    A = float(input("Digite a população do país A: "))
    B = float(input("Digite a população do país B: "))

    anos = calcular_anos(A, B)

    print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")