class Elevador:
    def __init__(self, andar_atual, total_andares, capacidade):
        self._andar_atual = andar_atual
        self._total_andares = total_andares
        self._capacidade = capacidade
        self._pessoas = 0

    @property
    def andar_atual(self):
        return self._andar_atual

    @property
    def total_andares(self):
        return self._total_andares

    @property
    def capacidade(self):
        return self._capacidade

    @property
    def pessoas(self):
        return self._pessoas

    def inicializar(self):
        self._andar_atual = 0
        self._pessoas = 0

    def entrar(self):
        if self._pessoas < self._capacidade:
            self._pessoas += 1
        else:
            print("Elevador cheio.")

    def sair(self):
        if self._pessoas > 0:
            self._pessoas -= 1
        else:
            print("Elevador vazio.")

    def escolher_andar(self, andar):
        if 0 <= andar <= self._total_andares:
            self._andar_atual = andar
        else:
            print("Andar inválido.")

    def subir(self):
        if self._andar_atual < self._total_andares:
            self._andar_atual += 1
        else:
            print("Elevador no último andar.")

    def descer(self):
        if self._andar_atual > 0:
            self._andar_atual -= 1
        else:
            print("Elevador no térreo, andar = 0.")

def menu():
    print("1 - Inicializar\n2 - Entrar\n3 - Sair\n4 - Subir\n5 - Descer\n6 - Escolher Andar\n7 - Sair")
    op = int(input("Digite uma das opções acima: "))
    return op

def main():
    elevador = Elevador(0, 10, 5)
    while True:
        opcao = menu()
        if opcao == 1:
            elevador.inicializar()
        elif opcao == 2:
            elevador.entrar()
        elif opcao == 3:
            elevador.sair()
        elif opcao == 4:
            elevador.subir()
        elif opcao == 5:
            elevador.descer()
        elif opcao == 6:
            andar = int(input("Digite o andar: "))
            elevador.escolher_andar(andar)
        elif opcao == 7:
            break
        else:
            print("Opção inválida. Tente novamente.")
        print(f"Andar atual: {elevador.andar_atual}\nPessoas: {elevador.pessoas}")

main()