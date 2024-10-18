def troca(lista):
    if not lista:
        return []
    x = len(lista)
    for i in range(x // 2):
        lista[i], lista[x - i - 1] = lista[x - i - 1], lista[i]
    return lista

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista_trocada = troca(lista)
    print(lista_trocada)

main()