import random

def random_():
    return random.randint(1, 100)

def main():
    while True:
        target = random_()
        cont = 0
        while True:
            i = int(input("Digite um numero entre 1 e 100: "))
            if i == target:
                print("Parabéns!")
                break
            else:
                cont += 1
                if cont == 10:
                    print(f'Máximo de tentativas alcançadas {cont} !!')
                    break
        
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa.")
            break

main()