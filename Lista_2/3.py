def procura(lst):
    cont = 0
    procura = input("Caracter a buscar:")
    for item in lst:
        for char in item:
            if char == procura:
                cont += 1
    return cont

def main():
    lista = ["banana", "maçã", "laranja", "morango"]
    print(lista)
    resultado = procura(lista)
    print(f"Caracter encontrado {resultado} vezes.")

main()
