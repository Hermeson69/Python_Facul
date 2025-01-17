
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
    def modelo(self, valor):
        self._modelo = valor
    
    @property
    def ano(self):
        return self._ano
    @ano.setter
    def ano(self, valor):
        self._ano = valor
    
    @property
    def placa(self):
        return self._placa
    @placa.setter
    def placa(self, valor):
        self._placa = valor
    
    @property
    def emprestado(self):
        return self._emprestado
    @emprestado.setter
    def emprestado(self, valor):
        self._emprestado = valor

    def __str__(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Placa: {self.placa}, Situação: {self.emprestado}"
    
class Emprestimo:
    def __init__(self):
       self._emprestado = {}
    
    def adicionar_emprestimo(self, carro, cliente):
        if carro.emprestado:
            print(f"O carro de modelo: {carro.modelo} já está emprestado")
        else:
            self._emprestado[carro.placa] = (carro, cliente)
            carro.emprestado = True
            print(f"Carro de modelo {carro.modelo} emprestado com sucesso para o cliente {cliente}")
    def devolver_carro(self, carro, cliente):
        if not carro.emprestado:
            print(f"Carro {carro.modelo}, não está emprestado")
        else:
            self._emprestado.pop(carro.placa, None)
            carro.emprestado = False
            print(f"Carro de modelo {carro.modelo} devolvido pelo cliente {cliente}")
    def imprimir_emprestimos(self):
        if not self._emprestado:
            print("Nem um carro emprestado")
        else:
            for placa, (carro, cliente) in self._emprestado.items():
                print(f"Carro de Placa: {placa}, de modelo: {carro.modelo} emprestado a {cliente}")

def main():
    carro1 = Carro("T-rex", 2022, "KKK-9999")
    carro2 = Carro("Supra", 1993, "b1g-b055")
    carro3 = Carro("R34", 2007, "KKK-6666")
    emprestimos = Emprestimo()
    emprestimos.adicionar_emprestimo(carro1, "Goku")
    emprestimos.adicionar_emprestimo(carro2, "Vejeta")
    emprestimos.adicionar_emprestimo(carro3, "Gohn")

    emprestimos.imprimir_emprestimos()

    emprestimos.devolver_carro(carro1, "Goku")

    emprestimos.imprimir_emprestimos()




main()