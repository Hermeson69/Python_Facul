class Elevador:
    def __init__(self, andar_atual, total_andares, capacidade):
        self._andar_atual = andar_atual
        self._total_andares = total_andares
        self._capacidade = capacidade
        self._pessoas = []
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
        self._pessoas = []
    def entrar(self, nome):
        if len(self._pessoas) < self._capacidade:
            self._pessoas.append(nome)
        else:
            print("Elevador cheio.")
    def sair(self, nome):
        if nome in self._pessoas:
            self._pessoas.remove(nome)
        else:
            print("Pessoa não está no elevador.")
    def escolher_andar(self, andar):
        if andar >= 0 and andar <= self._total_andares:
            self._andar_atual = andar
        elif andar < 0:
            print("Andar inválido.")
        elif andar > self._total_andares:
            print("Andar inválido.")
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
            nome = input("Digite o nome da pessoa: ")
            elevador.entrar(nome)
        elif opcao == 3:
            nome = input("Digite o nome da pessoa: ")
            elevador.sair(nome)
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