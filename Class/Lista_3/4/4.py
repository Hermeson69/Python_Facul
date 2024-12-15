class Televisao:
    def __init__(self, volume=0, canal=1):
        self._volume = volume
        self._canal = canal

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, valor):
        if 0 <= valor <= 100:
            self._volume = valor
        else:
            print("Volume inválido.")

    @property
    def canal(self):
        return self._canal

    @canal.setter
    def canal(self, valor):
        if 1 <= valor <= 100:
            self._canal = valor
        else:
            print("Canal inválido.")

    def aumentar_volume(self):
        if self._volume < 100:
            self._volume += 1

    def diminuir_volume(self):
        if self._volume > 0:
            self._volume -= 1

    def aumentar_canal(self):
        if self._canal < 100:
            self._canal += 1

    def diminuir_canal(self):
        if self._canal > 1:
            self._canal -= 1

    def escolher_canal(self, canal):
        self.canal = canal

    def consultar_volume(self):
        return self._volume

    def consultar_canal(self):
        return self._canal


class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao

   

def main():
    tv = Televisao()
    controle = ControleRemoto(tv)
    while True:
        print("\n1 - Aumentar Volume")
        print("2 - Diminuir Volume")
        print("3 - Aumentar Canal")
        print("4 - Diminuir Canal")
        print("5 - Escolher Canal")
        print("6 - Consultar Volume")
        print("7 - Consultar Canal")
        print("8 - Sair")
        opcao = int(input("Digite uma das opções acima: "))

        if opcao == 1:
            controle.televisao.aumentar_volume()
        elif opcao == 2:
            controle.televisao.diminuir_volume()
        elif opcao == 3:
            controle.televisao.aumentar_canal()
        elif opcao == 4:
            controle.televisao.diminuir_canal()
        elif opcao == 5:
            canal = int(input("Digite o canal: "))
            controle.televisao.escolher_canal(canal)
        elif opcao == 6:
            print(f"Volume atual: {controle.televisao.consultar_volume()}")
        elif opcao == 7:
            print(f"Canal atual: {controle.televisao.consultar_canal()}")
        elif opcao == 8:
            break
        else:
            print("Opção inválida.")
        print(f"Volume atual: {tv.volume}\nCanal atual: {tv.canal}")

main()
