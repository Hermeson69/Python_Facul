class Televisao:
    def __init__(self, volume, canal_atual):
        self._volume = volume
        self._canal_atual = canal_atual
    @property
    def volume(self):
        return self._volume
    @property
    def canal_atual(self):
        return self._canal_atual
    
    def aumentar_volume(self):
        if self._volume < 100:
            self._volume += 1
        else:
            print("Volume máximo.")
    
    def diminuir_volume(self):
        if self._volume == 100:
            print("Volume máximo.")
        elif self._volume > 0:
            self._volume -= 1
        else:
            print("Volume mínimo.")
    
    def aumentar_canal(self):
        if self._canal_atual < 100:
            self._canal_atual += 1
        else:
            print("Canal máximo.")
    
    def diminuir_canal(self):
        if self._canal_atual == 100:
            print("Canal máximo.")
        elif self._canal_atual > 0:
            self._canal_atual -= 1
        else:
            print("Canal mínimo.")
    
    def escolher_canal(self, canal):
        if canal >= 0 and canal <= 100:
            self._canal_atual = canal
        else:
            print("Canal inválido.")
    
def menu():
        print("1 - Aumentar Volume\n2 - Diminuir Volume\n3 - Aumentar Canal\n4 - Diminuir Canal\n5 - Escolher Canal\n6 - Sair")
        op = int(input("Digite uma das opções acima: "))
        return op
    
def main():
        tv = Televisao (0, 0)
        while True:
            opcao = menu()
            if opcao == 1:
                tv.aumentar_volume()
            elif opcao == 2:
                tv.diminuir_volume()
            elif opcao == 3:
                tv.aumentar_canal()
            elif opcao == 4:
                tv.diminuir_canal()
            elif opcao == 5:
                canal = int(input("Digite o canal: "))
                tv.escolher_canal(canal)
            elif opcao == 6:
                break
            else:
                print("Opção inválida.")
            print(f"Volume: {tv.volume}\nCanal: {tv.canal_atual}")

main()