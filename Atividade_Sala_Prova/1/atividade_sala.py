class Pessoa:
    def __init__(self, nome, idade): 
        self._nome = nome 
        self._idade = idade

    def exibir_dados(self): 
        print(f"Nome: {self._nome}") 
        print(f"Idade: {self._idade}")
        
class Estudante(Pessoa): 
    def __init__(self, nome, idade, curso): 
        super()._init_ (nome, idade) 
        self.curso = curso


    def exibir_dados(self): 
        print(f"Nome do Estudante:{self.nome}") 
        print(f"Idade do Estudante: {self.idade}") 
        print(f"Curso: {self.curso}")
        

pessoa1 = Pessoa("João", 25)
pessoa1.exibir_dados()

estudante1 = Estudante("Maria", 20, "Engenharia")
estudante1.exibir_dados()
# O erro se encontra na não ultilizaçaõ do @property para acessar o atributo privado;
# ou @setter para alterar o atributo privado.
# da mesma forma no exibir_dados dos estudantes que deveria ser self._nome e self._idade.
