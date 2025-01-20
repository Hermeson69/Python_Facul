from Usuarios.usuarios import Medico, Guiche, Enfermeiro, AtendenteFarmacia, Administrador
import os
import platform

class SistemaFarmacia:
    """Classe principal para gerenciar o sistema da farmácia."""

    def __init__(self):
        self.solicitacoes = []
        self.prescricoes = []
        self.guiche = Guiche("Guiche Principal", "00000000000") #Guiche "Fisico"
        self.consultas = []
        self.usuario_logado = None

        # Adiconado todos os usuarios para facilitar o uso;
        administrador = Administrador("Admin", "00000000001")
        self.movimentacoes = administrador.movimentacoes
        self.usuarios = administrador.usuarios
        self.usuarios.append(Enfermeiro("Mariana", "98765432100", "COREN5678"))
        atendente = AtendenteFarmacia("Ana", "11223344556")
        self.usuarios.append(atendente)
        self.usuarios.append(Medico("Dr. João", "12312312399", "CRM12345"))
        self.usuarios.append(Guiche("Carlos", "99887766554"))
        self.usuarios.append(administrador)
        # Adiconando medicamentos para faciliatr o uso
        self.guiche.registrar_paciente("José da Silva", "11122233344", 45)
        medicamentos_iniciais = {
            "Dipirona": 100,
            "Paracetamol": 80,
            "Amoxicilina": 50
        }
        for medicamento, quantidade in medicamentos_iniciais.items():
            atendente.adicionar_medicamento(medicamento, quantidade)
    # função básica para a limpagem do terminal após cada termino de usuario;
    def limpar_terminal(self):
        sistema = platform.system()
        if sistema == "Windows":
            os.system("cls") 
        else:
            os.system("clear")
    # Menu geral onde puxa os demais
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
                elif isinstance(self.usuario_logado, Guiche):
                    self.menu_guiche()
                elif isinstance(self.usuario_logado, Administrador):
                    self.menu_administrador()

    def login(self):
        cpf = input("CPF: ")
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                self.usuario_logado = usuario
                print(f"Bem-vindo, {usuario.nome}!")
                descricao = (f"Usuario {self.usuario_logado.nome} Logou no Sistema")
                self.movimentacoes.append(descricao)
                return
        print("Usuário não encontrado.")

    def menu_medico(self):
        while True:
            print(f"\n=== Menu Médico ({self.usuario_logado.nome}) ===")
            print("1. Listar Pacientes")
            print("2. Chamar Paciente")
            print("3. Realizar Consulta")
            print("4. Logout")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.usuario_logado.listar_pacientes()

            elif escolha == "2":
                self.usuario_logado.listar_pacientes()
                try:
                    idx = int(input("Número do Paciente: "))
                    print(self.usuario_logado.chamar_paciente(idx))
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")

            elif escolha == "3":
                cpf_paciente = input("CPF do Paciente: ")
                medicamento = input("Nome do Medicamento: ")
                try:
                    quantidade = int(input("Quantidade: "))
                    print(self.usuario_logado.realizar_consulta(self, cpf_paciente, medicamento, quantidade))
                    descricao = (f"Medico {self.usuario_logado.nome} realizou uma consulta para o paciente {cpf_paciente} e prescrevel o medicamento: {medicamento} em quantidade {quantidade} mg")
                    self.movimentacoes.append(descricao)
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para a quantidade.")

            elif escolha == "4":
                self.usuario_logado = None
                self.limpar_terminal()
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
                descricao = (f"Enfermero {self.usuario_logado.nome} solicitou medicamento para o paciente {nome_paciente}")
                self.movimentacoes.append(descricao)

            elif escolha == "2":
                self.usuario_logado = None
                self.limpar_terminal()
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_atendente(self):
        while True:
            print(f"\n=== Menu Atendente ({self.usuario_logado.nome}) ===")
            print("1. Atender Solicitação")
            print("2. Exibir Histórico de Movimentações")
            print("3. Ver Estoque de Medicamentos")
            print("4. Adicionar Medicamento ao Estoque")
            print("5. Logout")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                resultado = self.usuario_logado.atender_solicitacao(self)
                print(resultado)
                if "Solicitação atendida" in resultado:
                    descricao = (f"Atendente {self.usuario_logado.nome} atendeu a solicitação de medicamento.")
                    self.movimentacoes.append(descricao)

            elif escolha == "2":
                self.usuario_logado.exibir_historico()

            elif escolha == "3":
                medicamento = input("Nome do Medicamento: ")
                quantidade = self.usuario_logado.verificar_estoque(medicamento)
                if quantidade > 0:
                    print(f"Quantidade disponível de {medicamento}: {quantidade}")
                else:
                    print(f"{medicamento} não está disponível no estoque.")
                descricao = (f"Atendente {self.usuario_logado.nome} verificou o estoque do medicamento {medicamento}")
                self.movimentacoes.append(descricao)

            elif escolha == "4":
                medicamento = input("Nome do Medicamento: ")
                try:
                    quantidade = int(input("Quantidade: "))
                    self.usuario_logado.adicionar_medicamento(medicamento, quantidade)
                    print(f"{quantidade} unidades de {medicamento} adicionadas ao estoque.")
                    descricao = (f"Atendente {self.usuario_logado.nome}, cadastrou {medicamento} com quantidade {quantidade} na farmacia")
                    self.movimentacoes.append(descricao)
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para a quantidade.")

            elif escolha == "5":
                self.usuario_logado = None
                self.limpar_terminal()
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_guiche(self):
        while True:
            print(f"\n=== Menu Guichê ===")
            print("1. Registrar Paciente")
            print("2. Listar Pacientes")
            print("3. Enviar Paciente para Médico")
            print("4. Logout")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Nome do Paciente: ")
                cpf = input("CPF do Paciente: ")
                idade = int(input("Idade do Paciente: "))
                print(self.guiche.registrar_paciente(nome, cpf, idade))
                descricao = (f"O Guiche {self.usuario_logado.nome} cadastrou o paciente: {nome} CPF: {cpf} para atendimento")
                self.movimentacoes.append(descricao)

            elif escolha == "2":
                self.guiche.listar_pacientes()

            elif escolha == "3":
                cpf = input("CPF do Paciente: ")
                nome_medico = input("Nome do Médico: ")
                medico = None
                for u in self.usuarios:
                    if isinstance(u, Medico) and u.nome == nome_medico:
                        medico = u
                        break
                if medico:
                    print(self.guiche.enviar_paciente_para_medico(cpf, medico))
                    descricao = (f"O Guiche {self.usuario_logado.nome} enviou o paciente de CPF: {cpf} para o medico {medico.nome}")
                    self.movimentacoes.append(descricao)
                else:
                    print("Médico não encontrado.")

            elif escolha == "4":
                self.usuario_logado = None
                self.limpar_terminal()
                break

            else:
                print("Opção inválida. Tente novamente.")

    def menu_administrador(self):
        while True:
            print(f"\n=== Menu Administrador ({self.usuario_logado.nome}) ===")
            print("1. Gerenciar Usuários")
            print("2. Ver Relatórios")
            print("3. Logout")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.gerenciar_usuarios()

            elif escolha == "2":
                self.ver_relatorios()

            elif escolha == "3":
                self.usuario_logado = None
                self.limpar_terminal()
                break

            else:
                print("Opção inválida. Tente novamente.")

    def gerenciar_usuarios(self):
        while True:
            print("\n=== Gerenciar Usuários ===")
            print("1. Cadastrar Médico")
            print("2. Cadastrar Enfermeiro")
            print("3. Cadastrar Atendente de Farmácia")
            print("4. Cadastrar Guichê")
            print("5. Listar Usuários")
            print("6. Voltar")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Nome do Médico: ")
                cpf = input("CPF do Médico: ")
                crm = input("CRM do Médico: ")
                print(self.usuario_logado.cadastrar_medico(nome, cpf, crm))

            elif escolha == "2":
                nome = input("Nome do Enfermeiro: ")
                cpf = input("CPF do Enfermeiro: ")
                coren = input("COREN do Enfermeiro: ")
                print(self.usuario_logado.cadastrar_enfermeiro(nome, cpf, coren))

            elif escolha == "3":
                nome = input("Nome do Atendente de Farmácia: ")
                cpf = input("CPF do Atendente de Farmácia: ")
                print(self.usuario_logado.cadastrar_atendente_farmacia(nome, cpf))

            elif escolha == "4":
                nome = input("Nome do Guichê: ")
                cpf = input("CPF do Guichê: ")
                print(self.usuario_logado.cadastrar_guiche(nome, cpf))

            elif escolha == "5":
                self.usuario_logado.listar_usuarios()

            elif escolha == "6":
                self.limpar_terminal()
                break

            else:
                print("Opção inválida. Tente novamente.")

    def ver_relatorios(self):
        # Implementar a lógica para ver relatórios
        self.usuario_logado.movimentacoes_do_sistema()