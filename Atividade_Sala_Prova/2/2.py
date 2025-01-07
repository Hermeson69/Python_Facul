class Carro:
    def __init__(self, modelo, ano, placa):
        self._modelo = modelo
        self._ano = ano
        self._placa = placa
        self._emprestado = False

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, value):
        self._placa = value

    @property
    def emprestado(self):
        return self._emprestado

    @emprestado.setter
    def emprestado(self, value):
        self._emprestado = value

    def __str__(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Placa: {self.placa}, Emprestado: {self.emprestado}"

class Emprestimo:
    def __init__(self):
        self.emprestimos = {}

    def adicionar_emprestimo(self, carro, cliente):
        if carro.emprestado:
            print(f"O carro {carro.modelo} já está emprestado.")
        else:
            self.emprestimos[carro.placa] = (carro, cliente)
            carro.emprestado = True
            print(f"Empréstimo do carro {carro.modelo} para {cliente} realizado com sucesso.")

    def devolver_carro(self, carro):
        if not carro.emprestado:
            print(f"O carro {carro.modelo} não está emprestado.")
        else:
            self.emprestimos.pop(carro.placa, None)
            carro.emprestado = False
            print(f"Devolução do carro {carro.modelo} realizada com sucesso.")

    def imprimir_emprestimos(self):
        if not self.emprestimos:
            print("Nenhum empréstimo realizado.")
        else:
            for placa, (carro, cliente) in self.emprestimos.items():
                print(f"Carro com placa {placa} emprestado para {cliente}.")
                print(f"Modelo: {carro.modelo}, Cliente: {cliente}")

def main():
    carro1 = Carro("Fusca", 1980, "ABC-1234")
    carro2 = Carro("Gol", 2010, "XYZ-5678")
    carro3 = Carro("Civic", 2020, "DEF-9012")

    emprestimo = Emprestimo()

    emprestimo.adicionar_emprestimo(carro1, "João")
    emprestimo.adicionar_emprestimo(carro2, "Maria")
    emprestimo.adicionar_emprestimo(carro3, "Pedro")

    emprestimo.imprimir_emprestimos()

    emprestimo.devolver_carro(carro1)
    emprestimo.imprimir_emprestimos()

if __name__ == "__main__":
    main()
