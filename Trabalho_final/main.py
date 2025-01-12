import datetime
import abc

# Classe base para os usuários do sistema
class Usuario(abc.ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    @abc.abstractmethod
    def realizar_acao(self):
        pass

# Classe para Enfermeiros
class Enfermeiro(Usuario):
    def __init__(self, nome, cpf, registro_coren):
        super().__init__(nome, cpf)
        self.registro_coren = registro_coren

    def solicitar_medicamento(self, sistema, medicamento, quantidade, nome_paciente):
        sistema.solicitacoes.append({
            "enfermeiro": self.nome,
            "medicamento": medicamento,
            "paciente": nome_paciente,
            "quantidade": quantidade,
            "data": datetime.datetime.now()
        })
        return f"Enfermeiro {self.nome} solicitou {quantidade} unidades do medicamento {medicamento} para o paciente {nome_paciente}."

    def realizar_acao(self):
        print(f"{self.nome} (Enfermeiro) está gerenciando os cuidados médicos dos pacientes.")

# Classe para Atendentes da Farmácia
class AtendenteFarmacia(Usuario):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.estoque = {}
        self.historico = []

    def adicionar_medicamento(self, medicamento, quantidade):
        if medicamento in self.estoque:
            self.estoque[medicamento] += quantidade
        else:
            self.estoque[medicamento] = quantidade
        self.historico.append(f"Adicionado {quantidade} unidades de {medicamento} em {datetime.datetime.now()}")
        return f"Medicamento {medicamento} adicionado. Estoque atual: {self.estoque[medicamento]} unidades."

    def verificar_estoque(self, medicamento, quantidade):
        if medicamento in self.estoque and self.estoque[medicamento] >= quantidade:
            return True, f"Estoque disponível: {self.estoque[medicamento]} unidades de {medicamento}."
        else:
            return False, f"Estoque insuficiente para {medicamento}. Disponível: {self.estoque.get(medicamento, 0)} unidades."

    def atender_solicitacao(self, sistema):
        if not sistema.solicitacoes:
            return "Nenhuma solicitação pendente."

        solicitacao = sistema.solicitacoes.pop(0)
        medicamento = solicitacao["medicamento"]
        quantidade = solicitacao["quantidade"]
        enfermeiro = solicitacao["enfermeiro"]

        disponivel, mensagem = self.verificar_estoque(medicamento, quantidade)
        print(mensagem)  # Exibir status do estoque antes de decidir

        if disponivel:
            self.estoque[medicamento] -= quantidade
            self.historico.append(f"Entregue {quantidade} unidades de {medicamento} para {enfermeiro} em {datetime.datetime.now()}")
            return f"Solicitação atendida: {quantidade} unidades de {medicamento} entregues para {enfermeiro}. Estoque restante: {self.estoque[medicamento]} unidades."
        else:
            self.historico.append(f"Falha ao atender solicitação de {quantidade} unidades de {medicamento} para {enfermeiro} em {datetime.datetime.now()} - Estoque insuficiente")
            return f"Estoque insuficiente para atender a solicitação de {quantidade} unidades de {medicamento} feita por {enfermeiro}."

    def exibir_historico(self):
        if self.historico:
            print("Histórico de movimentações:")
            for registro in self.historico:
                print(registro)
        else:
            print("Nenhum registro no histórico.")

    def realizar_acao(self):
        print(f"{self.nome} (Atendente da Farmácia) está gerenciando os medicamentos.")

    def menu_atendente(self, sistema):
        while True:
            print("\n=== Menu Atendente ===")
            print("1. Listar Solicitações")
            print("2. Atender Solicitação")
            print("3. Exibir Histórico")
            print("4. Voltar ao Menu Principal")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                if sistema.solicitacoes:
                    print("Solicitações pendentes:")
                    for i, solicitacao in enumerate(sistema.solicitacoes):
                        print(f"{i + 1}. Enfermeiro: {solicitacao['enfermeiro']}, Medicamento: {solicitacao['medicamento']}, Quantidade: {solicitacao['quantidade']}, Paciente: {solicitacao['paciente']}, Data: {solicitacao['data']}")
                else:
                    print("Nenhuma solicitação pendente.")
            
            elif escolha == "2":
                if sistema.solicitacoes:
                    print("Solicitações pendentes:")
                    for i, solicitacao in enumerate(sistema.solicitacoes):
                        print(f"{i + 1}. Enfermeiro: {solicitacao['enfermeiro']}, Medicamento: {solicitacao['medicamento']}, Quantidade: {solicitacao['quantidade']}, Paciente: {solicitacao['paciente']}, Data: {solicitacao['data']}")
                    indice = int(input("Escolha o número da solicitação para atender: ")) - 1
                    if 0 <= indice < len(sistema.solicitacoes):
                        print(self.atender_solicitacao(sistema))
                    else:
                        print("Número de solicitação inválido.")
                else:
                    print("Nenhuma solicitação pendente.")
            
            elif escolha == "3":
                self.exibir_historico()
            
            elif escolha == "4":
                break
            
            else:
                print("Opção inválida. Tente novamente.")

# Classe para gerenciamento do sistema
class SistemaFarmacia:
    def __init__(self):
        self.usuarios = []
        self.solicitacoes = []

        # Usuários padrão
        self.usuarios.append(Enfermeiro("Carlos", "12345678901", "COREN1234"))
        self.usuarios.append(Enfermeiro("Mariana", "98765432100", "COREN5678"))
        atendente = AtendenteFarmacia("Ana", "11223344556")
        self.usuarios.append(atendente)

        # Medicamentos padrão
        medicamentos_iniciais = {
            "Dipirona": 100,
            "Paracetamol": 80,
            "Amoxicilina": 50,
            "Omeprazol": 30,
            "Ibuprofeno": 40,
            "Ranitidina": 20,
            "Azitromicina": 25,
            "Losartana": 35,
            "Metformina": 60,
            "Cetoconazol": 15
        }
        for medicamento, quantidade in medicamentos_iniciais.items():
            atendente.adicionar_medicamento(medicamento, quantidade)

    def adicionar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            self.usuarios.append(usuario)
            return f"Usuário {usuario.nome} adicionado ao sistema."
        else:
            return "Erro: o objeto não é um usuário válido."

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"Nome: {usuario.nome}, CPF: {usuario.cpf}, Tipo: {type(usuario).__name__}")

    def menu_interativo(self):
        while True:
            print("\n=== Menu Interativo ===")
            print("1. Adicionar Usuário")
            print("2. Listar Usuários")
            print("3. Adicionar Medicamento")
            print("4. Solicitar Medicamento (Enfermeiro)")
            print("5. Menu Atendente")
            print("6. Sair")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                tipo = input("Digite o tipo de usuário (enfermeiro/atendente): ").strip().lower()
                nome = input("Nome: ")
                cpf = input("CPF: ")

                if tipo == "enfermeiro":
                    registro_coren = input("Registro COREN: ")
                    self.adicionar_usuario(Enfermeiro(nome, cpf, registro_coren))
                elif tipo == "atendente":
                    self.adicionar_usuario(AtendenteFarmacia(nome, cpf))
                else:
                    print("Tipo de usuário inválido.")

            elif escolha == "2":
                self.listar_usuarios()

            elif escolha == "3":
                nome_atendente = input("Nome do Atendente: ")
                medicamento = input("Nome do Medicamento: ")
                quantidade = int(input("Quantidade: "))
                
                for usuario in self.usuarios:
                    if isinstance(usuario, AtendenteFarmacia) and usuario.nome == nome_atendente:
                        print(usuario.adicionar_medicamento(medicamento, quantidade))
                        break
                else:
                    print("Atendente não encontrado.")

            elif escolha == "4":
                nome_enfermeiro = input("Nome do Enfermeiro: ")
                medicamento = input("Nome do Medicamento: ")
                quantidade = int(input("Quantidade: "))

                for usuario in self.usuarios:
                    if isinstance(usuario, Enfermeiro) and usuario.nome == nome_enfermeiro:
                        nome_paciente = input("Nome do Paciente: ")
                        print(usuario.solicitar_medicamento(self, medicamento, quantidade, nome_paciente))
                        break
                else:
                    print("Enfermeiro não encontrado.")

            elif escolha == "5":
                nome_atendente = input("Nome do Atendente: ")

                for usuario in self.usuarios:
                    if isinstance(usuario, AtendenteFarmacia) and usuario.nome == nome_atendente:
                        usuario.menu_atendente(self)
                        break
                else:
                    print("Atendente não encontrado.")

            elif escolha == "6":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
def main():
    # Instanciando o sistema
    sistema = SistemaFarmacia()

    # Executando o menu interativo
    sistema.menu_interativo()

if __name__ == "__main__":
    main()
