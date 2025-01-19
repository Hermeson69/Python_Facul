import datetime
import abc

# Classe base para os usuários do sistema
class Usuario(abc.ABC):
    """Classe abstrata base para representar um usuário do sistema."""

    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("O nome deve ser uma string não vazia.")
        self._nome = value

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        if not isinstance(value, str) or len(value) != 11 or not value.isdigit():
            raise ValueError("CPF deve ser uma string de 11 dígitos numéricos.")
        self._cpf = value

    @abc.abstractmethod
    def realizar_acao(self):
        pass

# Classe para Pacientes
class Paciente(Usuario):
    """Classe para representar um paciente."""

    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf)
        self.idade = idade

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("A idade deve ser um número inteiro não negativo.")
        self._idade = value

    def realizar_acao(self):
        print(f"{self.nome} (Paciente) está aguardando atendimento.")

# Classe para Médicos
class Medico(Usuario):
    """Classe para representar um médico."""

    def __init__(self, nome: str, cpf: str, crm: str):
        super().__init__(nome, cpf)
        self.crm = crm
        self._pacientes = {}

    @property
    def crm(self) -> str:
        return self._crm

    @crm.setter
    def crm(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("O CRM deve ser não Pode ser vazi0.")
        self._crm = value

    @property
    def pacientes(self):
        return self._pacientes

    def listar_pacientes(self):
        if not self._pacientes:
            print("Nenhum paciente na lista.")
        else:
            print("Pacientes na lista:")
            for idx, (cpf, paciente) in enumerate(self._pacientes.items(), start=1):
                print(f"{idx}. Nome: {paciente.nome}, CPF: {cpf}, Idade: {paciente.idade}")

    def chamar_paciente(self, indice: int) -> str:
        if not self._pacientes:
            return "Nenhum paciente na lista."

        pacientes_lista = list(self._pacientes.values())
        indice -= 1  # Adjust for 1-based index
        if indice < 0 or indice >= len(pacientes_lista):
            return "Índice de paciente inválido."

        paciente = pacientes_lista[indice]
        return f"Paciente {paciente.nome}, por favor, dirija-se à sala do Dr. {self.nome}."

    def prescrever_medicamento(self, sistema, medicamento: str, quantidade: int, cpf_paciente: str) -> str:
        paciente = self._pacientes.get(cpf_paciente)
        if not paciente:
            return "Paciente não encontrado."

        if not isinstance(medicamento, str) or not medicamento.strip():
            return "Nome do medicamento inválido."
        if not isinstance(quantidade, int) or quantidade <= 0:
            return "Quantidade de medicamento inválida."

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

class Guiche(Usuario):
    """Classe para representar um guichê de atendimento."""

    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)
        self._pacientes = {}

    def registrar_paciente(self, nome: str, cpf: str, idade: int) -> str:
        if not isinstance(nome, str) or not nome.strip():
            return "Nome inválido."
        if not isinstance(cpf, str) or len(cpf) != 11 or not cpf.isdigit():
            return "CPF inválido."
        if not isinstance(idade, int) or idade < 0:
            return "Idade inválida."

        if cpf in self._pacientes:
            return "Paciente já registrado."
        self._pacientes[cpf] = Paciente(nome, cpf, idade)
        return f"Paciente {nome} registrado com sucesso."

    def listar_pacientes(self):
        if not self._pacientes:
            print("Nenhum paciente registrado.")
        else:
            print("Pacientes registrados:")
            for cpf, paciente in self._pacientes.items():
                print(f"Nome: {paciente.nome}, CPF: {cpf}, Idade: {paciente.idade}")

    def obter_paciente(self, cpf: str) -> Paciente:
        return self._pacientes.get(cpf)

    def enviar_paciente_para_medico(self, cpf: str, medico: Medico) -> str:
        paciente = self._pacientes.get(cpf)
        if paciente:
            medico._pacientes[cpf] = paciente
            medico.listar_pacientes()  # Atualiza a lista de pacientes do médico
            return f"Paciente {paciente.nome} enviado para o Dr. {medico.nome}."
        return "Paciente não encontrado."

    def realizar_acao(self):
        print(f"{self.nome} (Guichê) está gerenciando o atendimento dos pacientes.")

# Classe para Enfermeiros
class Enfermeiro(Usuario):
    """Classe para representar um enfermeiro."""

    def __init__(self, nome: str, cpf: str, registro_coren: str):
        super().__init__(nome, cpf)
        self.registro_coren = registro_coren

    @property
    def registro_coren(self) -> str:
        return self._registro_coren

    @registro_coren.setter
    def registro_coren(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("O registro do COREN não Pode ser vazi0.")
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
        if not isinstance(medicamento, str) or not medicamento.strip():
            return "Nome do medicamento inválido."
        if not isinstance(quantidade, int) or quantidade <= 0:
            return "Quantidade de medicamento inválida."

        if medicamento in self._estoque:
            self._estoque[medicamento] += quantidade
        else:
            self._estoque[medicamento] = quantidade
        self._historico.append(f"Adicionado {quantidade} unidades de {medicamento} em {datetime.datetime.now()}")
        return f"Medicamento {medicamento} adicionado. Estoque atual: {self._estoque[medicamento]} unidades."

    def verificar_estoque(self, medicamento: str) -> int:
        if not isinstance(medicamento, str) or not medicamento.strip():
            return 0
        quantidade_total = self._estoque.get(medicamento, 0)
        return quantidade_total



    def atender_solicitacao(self, sistema):
        if not sistema.solicitacoes:
            return "Nenhuma solicitação pendente."

        solicitacao = sistema.solicitacoes.pop(0)
        medicamento = solicitacao["medicamento"]
        quantidade = solicitacao["quantidade"]
        enfermeiro = solicitacao["enfermeiro"]

        disponivel = self.verificar_estoque(medicamento)
        print(f"[DEBUG] Estoque antes da solicitação: {disponivel} unidades de {medicamento}. Solicitado: {quantidade} unidades.")
        
        medicamentos_iniciais = {
            "Dipirona": 100,
            "Paracetamol": 80,
            "Amoxicilina": 50
        }

        if medicamento in medicamentos_iniciais:
            print(f"[DEBUG] Medicamento {medicamento} é inicial e será descontado do estoque.")

        if disponivel >= quantidade:
            self._estoque[medicamento] -= quantidade
            self._historico.append(f"Entregue {quantidade} unidades de {medicamento} para {enfermeiro} em {datetime.datetime.now()}")
            print(f"[DEBUG] Estoque atualizado: {self._estoque[medicamento]} unidades restantes de {medicamento}.")
            return f"Solicitação atendida: {quantidade} unidades de {medicamento} entregues para {enfermeiro}. Estoque restante: {self._estoque[medicamento]} unidades."
        else:
            self._historico.append(f"Falha ao atender solicitação de {quantidade} unidades de {medicamento} para {enfermeiro} em {datetime.datetime.now()} - Estoque insuficiente")
            print(f"[DEBUG] Estoque insuficiente: {disponivel} unidades de {medicamento}.")
            return f"Estoque insuficiente para atender a solicitação de {quantidade} unidades de {medicamento} feita por {enfermeiro}."

    def exibir_historico(self):
        if self._historico:
            print("Histórico de movimentações:")
            for registro in self._historico:
                print(registro)
        else:
            print("Nenhum registro no histórico.")

    def realizar_acao(self):
        print(f"{self.nome} (Atendente) está gerenciando o estoque e as solicitações.")
class Administrador(Usuario):
    """Classe para representar um administrador do sistema."""

    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)
        self._usuarios = []
        self._movimentacoes = []

    @property
    def usuarios(self):
        return self._usuarios
    @property
    def movimentacoes(self):
        return self._movimentacoes

    def cadastrar_usuario(self, usuario: Usuario) -> str:
        if not isinstance(usuario, Usuario):
            return "Usuário inválido."
        self._usuarios.append(usuario)
        return f"Usuário {usuario.nome} cadastrado com sucesso."

    def cadastrar_guiche(self, nome: str, cpf: str) -> str:
        guiche = Guiche(nome, cpf)
        return self.cadastrar_usuario(guiche)

    def cadastrar_medico(self, nome: str, cpf: str, crm: str) -> str:
        medico = Medico(nome, cpf, crm)
        return self.cadastrar_usuario(medico)

    def cadastrar_atendente_farmacia(self, nome: str, cpf: str) -> str:
        atendente = AtendenteFarmacia(nome, cpf)
        return self.cadastrar_usuario(atendente)

    def cadastrar_enfermeiro(self, nome: str, cpf: str, registro_coren: str) -> str:
        enfermeiro = Enfermeiro(nome, cpf, registro_coren)
        return self.cadastrar_usuario(enfermeiro)
    
    def registrar_movimentacao(self, descricao: str):
        self._movimentacoes.append(f"{descricao} em {datetime.datetime.now()}")

    def movimentacoes_do_sistema(self):
        if self._movimentacoes:
            print("Movimentações:")
            for movimentacao in self._movimentacoes:
                print(movimentacao)
        else:
            print("Nenhuma movimentação registrada.")


    def listar_usuarios(self):
        if not self._usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("Usuários cadastrados:")
            for idx, usuario in enumerate(self._usuarios, start=1):
                print(f"{idx}. Nome: {usuario.nome}, CPF: {usuario.cpf}, Tipo: {type(usuario).__name__}")

    def realizar_acao(self):
        print(f"{self.nome} (Administrador) está gerenciando o sistema.")