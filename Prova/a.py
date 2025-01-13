# import abc


# num = int(input("Digite um numero: "))

# anterior =  num
# estimativa = 1

# while estimativa != anterior:
#     anterior = estimativa
#     estimativa = (estimativa + (num/estimativa))/2
    
# print(estimativa)

# def achar_primo(num):
#     return all(num % i != 0 for i in range(2, num))

# num = int(input("Digite um numero: "))
# if achar_primo(num):
#     print("Numero primo")
# else:
#     print("Numero não primo")

# def achar_primo(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return  True

# num = int(input("Digite um numero: "))
# if achar_primo(num):
#     print("Numero primo")
# else:
#     print("Numero não primo")

# def calcular_anos(X, Y):
#     anos = 0
#     while X <= Y:
#         X = X + X * 0.03
#         Y = Y + Y * 0.015
#         anos += 1
#     return anos

# def valor_serie(n):
#     soma = 0
#     for i in range (1, n + 1):
#         soma += i / (2* i -1)

#     return soma

# num = int(input("Digite um numero: "))
# print(valor_serie(num))

# def raiz_quadrada(numero):
#     anterior = numero
#     estimativa = 1

#     while estimativa != anterior:
#         anterior = estimativa
#         estimativa = (estimativa + (numero / estimativa)) / 2
    
#     return estimativa

# def pitagoras(a, b):
#     c_quadrado = (a * a) + (b * b) 
#     return raiz_quadrada(c_quadrado)  

# a = float(input("Digite o valor de a: "))
# b = float(input("Digite o valor de b: "))
# c = pitagoras(a, b)
# print(f"O valor de c é: {c}")


# class Produto:
#     def __init__(self, nome, preco):
#         self._nome = nome
#         self._preco = preco

#     @property
#     def nome(self):
#         return self._nome

#     @property
#     def preco(self):
#         return self._preco

#     @preco.setter
#     def preco(self, valor):
#         if valor < 0:
#             raise ValueError("Preço não pode ser negativo")
#         self._preco = valor

# produto = Produto("Notebook", 2500.00)
# print(f"Produto: {produto.nome}, Preço: {produto.preco}")

# novo_preco = -100
# try:
#     produto.preco = novo_preco  
# except ValueError as e:
#     print(e)

# print(f"Produto: {produto.nome}, Preço: {produto.preco}")



# class Funcionario:
#     def __init__(self, nome, salario):
#         self._nome = nome
#         self._salario = salario

#     @property
#     def nome(self):
#         return self._nome

#     @property
#     def salario(self):
#         return self._salario

#     @salario.setter
#     def salario(self, valor):
#         if valor < 1500:
#             raise ValueError("Salario não pode ser menor que 1500")
#         self._salario = valor

# produto = Funcionario("Notebook", 1520.00)
# print(f"Funcionario: {produto.nome}, Salario R$: {produto.salario}")

# novo_salario = 2500
# try:
#     produto.salario = novo_salario  
# except ValueError as e:
#     print(e)

# print(f"Funcionario: {produto.nome}, Salario R$: {produto.salario}")

# # Herança simples
# class Veiculo:
#     def __init__(self, marca, ano):
#         self._marca = marca
#         self._ano = ano
    
#     @property
#     def marca(self):
#         return self._marca
    
#     @property
#     def ano(self):
#         return self._ano

#     def informacoes(self):
#         return f'Veículo da marca {self._marca} do ano {self._ano}'
    
# class Carro(Veiculo):
#     def __init__(self, marca, ano, quant_portas):
#         super().__init__(marca, ano)
#         self._quant_portas = quant_portas
    
#     @property
#     def quant_portas(self):
#         return self._quant_portas

#     def informacoes(self):
#         return f'Carro da marca {self._marca} do ano {self._ano} com {self._quant_portas} portas'

# veiculo = Veiculo("Toyota", 2020)
# print(veiculo.informacoes())

# carro = Carro("Honda", 2021, 4)
# print(carro.informacoes())

# class Nadador:
#     def nadar(self):
#         print("Estou nadando!")

# class Corredor:
#     def correr(self):
#         print("Estou correndo!")

# class Triatleta(Nadador, Corredor):
#     pass

# # Test the Triatleta class
# triatleta = Triatleta()
# triatleta.nadar()
# triatleta.correr()

# class Forma:
#     def area(self):
#         pass

# class Circulo(Forma):
#     def __init__(self, raio):
#         self.raio = raio

#     def area(self):
#         return 3.14 * self.raio ** 2

# class Retangulo(Forma):
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def area(self):
#         return self.largura * self.altura

# def exibir_area(forma):
#     print(f'A área é: {forma.area()}')

# # Demonstrando polimorfismo
# formas = [Circulo(5), Retangulo(4, 6)]

# for forma in formas:
#     exibir_area(forma)

# class Animal(abc.ABC):
#     def __init__(self, nome):
#         self._nome = nome

#     @property
#     def nome(self):
#         return self._nome

#     @abc.abstractmethod
#     def falar(self):
#         pass

#     @abc.abstractmethod
#     def andar(self):
#         pass

# class Cachorro(Animal):
#     def __init__(self, nome):
#         super().__init__(nome)

#     def falar(self):
#         print("auau")

#     def andar(self):
#         print("andando")

# class Gato(Animal):
#     def __init__(self, nome):
#         super().__init__(nome)

#     def falar(self):
#         print("Miau")

#     def andar(self):
#         print("andando")


# # Test the Cachorro class
# cachorro = Cachorro("Rex")
# gato = Gato("Marcao gay")
# print(f'Nome: {cachorro.nome}')
# cachorro.falar()
# cachorro.andar()
# print(f'Nome: {gato.nome}')
# gato.falar()
# gato.andar()

# class Pagamento (abc.ABC):
#     @abc.abstractmethod
#     def autentica(self):
#         pass
#     @abc.abstractmethod
#     def processar_pagamento(self):
#         pass

# class CartaoCredito(Pagamento):
#     def __init__(self, numero_cartao):
#         self._numero_cartao = numero_cartao
#     @property
#     def numero_cartao(self):
#         return self._numero_cartao
    
#     def autentica(self):
#         if len(self.numero_cartao) == 16 and self.numero_cartao.isdigit():
#              print("Cartão autorizado")
#         else:
#             print("Número do cartão inválido")

#     def processar_pagamento(self):
#         print("Pagamento processado com cartão de crédito")
# class PIX(Pagamento):
#     def __init__(self, chave_pix):
#         self._chave_pix = chave_pix
#     @property
#     def chave_pix(self):
#         return self._chave_pix
    
#     def autentica(self):
#         if isinstance(self.chave_pix, str) and self.chave_pix:
#              print("Pix valido")
#         else:
#             print("Pix inválido")

#     def processar_pagamento(self):
#         print("Pagamento processado com Pix")

# cartao = CartaoCredito("1234567812345678")
# pix = PIX("chave_pix_valida")

# cartao.autentica()
# cartao.processar_pagamento()

# pix.autentica()
# pix.processar_pagamento()

