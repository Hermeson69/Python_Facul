import datetime
import abc

# Classe base para os usuários do sistema
class Usuario(abc.ABC):
    """Classe abstrata base para representar um usuário do sistema."""

    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str):
        if not value.strip():
            raise ValueError("O nome não pode ser vazio.")
        self._nome = value

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        if len(value) != 11 or not value.isdigit():
            raise ValueError("CPF deve ter 11 dígitos numéricos.")
        self._cpf = value

    @abc.abstractmethod
    def realizar_acao(self):
        pass

# Classe para Pacientes
class Paciente(Usuario):
    """Classe para representar um paciente."""

    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)

# Classe para Médicos
class Medico(Usuario):
    """Classe para representar um médico."""

    def __init__(self, nome: str, cpf: str, crm: str):
        super().__init__(nome, cpf)
        self._crm = crm
        self._pacientes = {}

    @property
    def crm(self) -> str:
        return self._crm

    @crm.setter
    def crm(self, value: str):
        if not value.strip():
            raise ValueError("O CRM não pode ser vazio.")
        self._crm = value

    @property
    def pacientes(self):
        return self._pacientes

    def chamar_paciente(self, cpf_paciente: str) -> str:
        paciente = self._pacientes.get(cpf_paciente)
        if paciente:
            return f"Paciente {paciente.nome}, por favor, dirija-se à sala do Dr. {self.nome}."
        return "Paciente não encontrado."

    def prescrever_medicamento(self, sistema, medicamento: str, quantidade: int, cpf_paciente: str) -> str:
        paciente = self._pacientes.get(cpf_paciente)
        if not paciente:
            return "Paciente não encontrado."

        prescricao = {
            "medico": self.nome,
            "medicamento": medicamento,
            "paciente": paciente.nome,
            "quantidade": quantidade,
            "data": datetime.datetime.now()
        }
        sistema.prescricoes.append(prescricao)
        return f"Prescrição registrada: {prescricao}"

    def realizar_consulta(self, sistema, cpf_paciente: str, medicamento: str, quantidade: int) -> str:
        paciente = sistema.guiche.obter_paciente(cpf_paciente)
        if not paciente:
            return "Paciente não encontrado."

        self._pacientes[cpf_paciente] = paciente
        sistema.consultas.append({
            "medico": self.nome,
            "paciente": paciente.nome,
            "data": datetime.datetime.now()
        })
        return self.prescrever_medicamento(sistema, medicamento, quantidade, cpf_paciente)

    def realizar_acao(self):
        print(f"{self.nome} (Médico) está gerenciando os cuidados médicos dos pacientes.")

# Classe para Enfermeiros
class Enfermeiro(Usuario):
    """Classe para representar um enfermeiro."""

    def __init__(self, nome: str, cpf: str, registro_coren: str):
        super().__init__(nome, cpf)
        self._registro_coren = registro_coren

    @property
    def registro_coren(self) -> str:
        return self._registro_coren

    @registro_coren.setter
    def registro_coren(self, value: str):
        if not value.strip():
            raise ValueError("O registro do COREN não pode ser vazio.")
        self._registro_coren = value

    def pegar_prescricao(self, sistema, nome_paciente: str) -> dict:
        for prescricao in sistema.prescricoes:
            if prescricao["paciente"] == nome_paciente:
                return prescricao
        return None

    def solicitar_medicamento(self, sistema, nome_paciente: str):
        prescricao = self.pegar_prescricao(sistema, nome_paciente)
        if prescricao:
            sistema.solicitacoes.append({
                "enfermeiro": self.nome,
                "medicamento": prescricao["medicamento"],
                "paciente": nome_paciente,
                "quantidade": prescricao["quantidade"],
                "data": datetime.datetime.now()
            })
            return f"Enfermeiro {self.nome} solicitou {prescricao['quantidade']} unidades do medicamento {prescricao['medicamento']} para o paciente {nome_paciente}."
        return f"Nenhuma prescrição encontrada para o paciente {nome_paciente}."

    def realizar_acao(self):
        print(f"{self.nome} (Enfermeiro) está gerenciando os cuidados médicos dos pacientes.")

# Classe para Guichê de Atendimento
class Guiche:
    """Classe para gerenciar o registro e listagem de pacientes."""

    def __init__(self):
        self.pacientes = {}

    def registrar_paciente(self, nome: str, cpf: str) -> str:
        if cpf not in self.pacientes:
            self.pacientes[cpf] = Paciente(nome, cpf)
            return f"Paciente {nome} registrado com sucesso."
        return f"Paciente {nome} já está registrado."

    def listar_pacientes(self):
        if self.pacientes:
            print("Pacientes registrados:")
            for cpf, paciente in self.pacientes.items():
                print(f"Nome: {paciente.nome}, CPF: {cpf}")
        else:
            print("Nenhum paciente registrado.")

    def obter_paciente(self, cpf: str) -> Paciente:
        return self.pacientes.get(cpf, None)

class AtendenteFarmacia(Usuario):
    """Classe para gerenciar o estoque e solicitações de medicamentos."""

    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)
        self._estoque = {}
        self._historico = []

    @property
    def estoque(self):
        return self._estoque

    @property
    def historico(self):
        return self._historico

    def adicionar_medicamento(self, medicamento: str, quantidade: int):
        if medicamento in self._estoque:
            self._estoque[medicamento] += quantidade
        else:
            self._estoque[medicamento] = quantidade
        self._historico.append(f"Adicionado {quantidade} unidades de {medicamento} em {datetime.datetime.now()}")
        return f"Medicamento {medicamento} adicionado. Estoque atual: {self._estoque[medicamento]} unidades."

    def verificar_estoque(self, medicamento: str, quantidade: int):
        if medicamento in self._estoque and self._estoque[medicamento] >= quantidade:
            return True, f"Estoque disponível: {self._estoque[medicamento]} unidades de {medicamento}."
        return False, f"Estoque insuficiente para {medicamento}. Disponível: {self._estoque.get(medicamento, 0)} unidades."

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
            self._estoque[medicamento] -= quantidade
            self._historico.append(f"Entregue {quantidade} unidades de {medicamento} para {enfermeiro} em {datetime.datetime.now()}")
            return f"Solicitação atendida: {quantidade} unidades de {medicamento} entregues para {enfermeiro}. Estoque restante: {self._estoque[medicamento]} unidades."
        else:
            self._historico.append(f"Falha ao atender solicitação de {quantidade} unidades de {medicamento} para {enfermeiro} em {datetime.datetime.now()} - Estoque insuficiente")
            return f"Estoque insuficiente para atender a solicitação de {quantidade} unidades de {medicamento} feita por {enfermeiro}."

    def exibir_historico(self):
        if self._historico:
            print("Histórico de movimentações:")
            for registro in self._historico:
                print(registro)
        else:
            print("Nenhum registro no histórico.")

    # Implementando o método abstrato
    def realizar_acao(self):
        print(f"{self.nome} (Atendente) está gerenciando o estoque e as solicitações.")


# Classe para Sistema de Farmácia
class SistemaFarmacia:
    """Classe principal para gerenciar o sistema da farmácia."""

    def __init__(self):
        self.usuarios = []
        self.solicitacoes = []
        self.prescricoes = []
        self.consultas = []
        self.usuario_logado = None
        self.guiche = Guiche()

        # Usuários padrão
        self.usuarios.append(Enfermeiro("Mariana", "98765432100", "COREN5678"))
        atendente = AtendenteFarmacia("Ana", "11223344556")
        self.usuarios.append(atendente)
        self.usuarios.append(Medico("Dr. João", "12312312399", "CRM12345"))

        # Medicamentos padrão
        medicamentos_iniciais = {
            "Dipirona": 100,
            "Paracetamol": 80,
            "Amoxicilina": 50
        }
        for medicamento, quantidade in medicamentos_iniciais.items():
            atendente.adicionar_medicamento(medicamento, quantidade)

    def menu_interativo(self):
        while True:
            if not self.usuario_logado:
                print("\n=== Menu Principal ===")
                print("1. Login")
                print("2. Sair")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    self.login()
                elif escolha == "2":
                    print("Saindo do sistema...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                if isinstance(self.usuario_logado, Medico):
                    self.menu_medico()
                elif isinstance(self.usuario_logado, Enfermeiro):
                    self.menu_enfermeiro()
                elif isinstance(self.usuario_logado, AtendenteFarmacia):
                    self.menu_atendente()

    def login(self):
        cpf = input("CPF: ")
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                self.usuario_logado = usuario
                print(f"Bem-vindo, {usuario.nome}!")
                return
        print("Usuário não encontrado.")

    def menu_medico(self):
        while True:
            print(f"\n=== Menu Médico ({self.usuario_logado.nome}) ===")
            print("1. Chamar Paciente")
            print("2. Realizar Consulta")
            print("3. Logout")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                cpf_paciente = input("CPF do Paciente: ")
                print(self.usuario_logado.chamar_paciente(cpf_paciente))

            elif escolha == "2":
                cpf_paciente = input("CPF do Paciente: ")
                medicamento = input("Nome do Medicamento: ")
                quantidade = int(input("Quantidade: "))
                print(self.usuario_logado.realizar_consulta(self, cpf_paciente, medicamento, quantidade))

            elif escolha == "3":
                self.usuario_logado = None
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_enfermeiro(self):
        while True:
            print(f"\n=== Menu Enfermeiro ({self.usuario_logado.nome}) ===")
            print("1. Solicitar Medicamento")
            print("2. Logout")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome_paciente = input("Nome do Paciente: ")
                print(self.usuario_logado.solicitar_medicamento(self, nome_paciente))

            elif escolha == "2":
                self.usuario_logado = None
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_atendente(self):
        while True:
            print(f"\n=== Menu Atendente ({self.usuario_logado.nome}) ===")
            print("1. Atender Solicitação")
            print("2. Exibir Histórico de Movimentações")
            print("3. Logout")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                print(self.usuario_logado.atender_solicitacao(self))

            elif escolha == "2":
                self.usuario_logado.exibir_historico()

            elif escolha == "3":
                self.usuario_logado = None
                break

            else:
                print("Opção inválida. Tente novamente.")

# Exemplo de uso
def main():
    sistema = SistemaFarmacia()
    sistema.menu_interativo()


main()