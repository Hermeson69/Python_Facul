import datetime
import os
import platform
from abc import ABC, abstractmethod

# Interface para usuários
class Usuario(ABC):
    @abstractmethod
    def mostrar_dados(self):
        pass

# Classe base para Pessoa
class Pessoa(Usuario):
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def mostrar_dados(self):
        print(f"👤 Nome: {self.nome}")


# Classe para Gerente, herdando de Pessoa
class Gerente(Pessoa):
    _credenciais = {"admin": "senha123"}  # Nome de usuário e senha de exemplo

    def __init__(self, nome, nivel):
        super().__init__(nome)
        self._nivel = nivel

    @property
    def nivel(self):
        return self._nivel

    def autenticar(self, usuario, senha):
        """Método de instância para autenticar um gerente."""
        if Gerente._credenciais.get(usuario) == senha:
            print("Autenticação realizada com sucesso!")
            return True
        print("Usuário ou senha inválidos.")
        return False

    def cadastrar_gerente(self):
        """Método de instância para cadastrar um novo gerente."""
        usuario = input("Digite o nome de usuário para o novo gerente: ")
        if usuario in Gerente._credenciais:
            print("Usuário já existe!")
            return
        senha = input("Digite a senha para o novo gerente: ")
        Gerente._credenciais[usuario] = senha
        print(f"Gerente {usuario} cadastrado com sucesso!")

    def listar_alunos(self, sistema):
        """Lista todos os alunos cadastrados no sistema."""
        sistema.listar_alunos()

    def registrar_frequencia(self, sistema, aluno_id):
        """Registra a frequência de um aluno."""
        aluno = sistema.buscar_aluno_por_id(aluno_id)
        if aluno:
            data = datetime.datetime.now()
            aluno.frequencia.registrar_presenca(data)
            print(f"Frequência registrada para o aluno {aluno.nome} no dia {data.strftime('%d/%m/%Y')}.")
        else:
            print("Aluno não encontrado.")
            

# Classe para Controle de Frequência
class Frequencia:
    def __init__(self):
        self._presencas = {}

    @property
    def presencas(self):
        return self._presencas

    def registrar_presenca(self, data):
        data_str = data.strftime('%d/%m/%Y')
        if data_str not in self._presencas:
            self._presencas[data_str] = 0
        self._presencas[data_str] += 1

    def exibir_frequencia(self):
        print("\n----- FREQUÊNCIA -----")
        for data, count in self._presencas.items():
            print(f"Data: {data} - Presenças: {count}")
            

# Classe para Pagamento
class Pagamento:
    def __init__(self):
        self._historico = []

    @property
    def historico(self):
        return self._historico

    def registrar_pagamento(self, valor, preco_plano, data=None):
        if valor != preco_plano:
            print(f"Erro: O valor do pagamento (R$ {valor:.2f}) não corresponde ao preço do plano (R$ {preco_plano:.2f}).")
            return False

        data = data or datetime.datetime.now()
        
        # Verificar se há um último pagamento e se o prazo de 30 dias já expirou
        if self._historico:
            ultimo_pagamento = self._historico[-1]["data"]
            dias_desde_ultimo = (data - ultimo_pagamento).days
            if dias_desde_ultimo < 30:
                print(f"Erro: O pagamento só pode ser feito após 30 dias do último pagamento. Faltam {30 - dias_desde_ultimo} dias.")
                return False

        # Registrar o pagamento
        self._historico.append({"valor": valor, "data": data})
        print(f"Pagamento de R$ {valor:.2f} registrado em {data.strftime('%d/%m/%Y')}.")
        return True

    def exibir_historico(self):
        #metodo para exibir o historico de pagamentos
        print("\n----- HISTÓRICO DE PAGAMENTOS -----")
        for pagamento in self._historico:
            print(f"Valor: R$ {pagamento['valor']:.2f} - Data: {pagamento['data'].strftime('%d/%m/%Y')}")#imprime o valor e a data do pagamento

    def verificar_inadimplencia(self, dias_tolerancia=30):
        if not self._historico:
            return True
        ultimo_pagamento = self._historico[-1]["data"]
        return (datetime.datetime.now() - ultimo_pagamento).days > dias_tolerancia


# Classe para Plano
class Plano:
    def __init__(self, nome, preco, descricao):
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def descricao(self):
        return self._descricao

    def mostrar_detalhes(self):
        print(f"Plano: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Descrição: {self.descricao}")
        

# Classe para Aluno
class Aluno(Pessoa):
    ultimo_id = 0

    def __init__(self, nome, plano):
        super().__init__(nome)
        Aluno.ultimo_id += 1
        self._id = f"{Aluno.ultimo_id:03d}"
        self._plano = plano
        self._frequencia = Frequencia()
        self._pagamento = Pagamento()
        self._status_matricula = True

    @property
    def id(self):
        return self._id

    @property
    def plano(self):
        return self._plano

    @plano.setter
    def plano(self, novo_plano):
        self._plano = novo_plano

    @property
    def frequencia(self):
        return self._frequencia

    @property
    def pagamento(self):
        return self._pagamento

    @property
    def status_matricula(self):
        return self._status_matricula

    @status_matricula.setter
    def status_matricula(self, status):
        self._status_matricula = status

    def cancelar_matricula(self):
        if self._status_matricula:
            self._status_matricula = False
            print("Matrícula cancelada com sucesso.")
        else:
            print("A matrícula já está cancelada.")

    def reativar_matricula(self):
        if not self._status_matricula:
            self._status_matricula = True
            print("Matrícula reativada com sucesso.")
        else:
            print("A matrícula já está ativa.")
        
    def mostrar_dados(self):
        print("\n-------------------------")
        print(f"📌 ID: {self.id}")
        super().mostrar_dados()
        print(f"🎓 Plano: {self.plano.nome} (R$ {self.plano.preco:.2f})")
        print(f"🔄 Status: {'Ativo' if self.status_matricula else 'Cancelado'}")
        print("-------------------------")


# Classe para Relatórios
class Relatorio:
    @staticmethod
    def gerar_relatorio_inadimplentes(sistema):
        print("\n📊 ----- RELATÓRIO DE INADIMPLENTES ----- 📊")
        inadimplentes = [
            aluno for aluno in sistema.alunos
            if aluno.pagamento.verificar_inadimplencia()
        ]
        if inadimplentes:
            print("\n⚠️  Alunos com pagamentos pendentes:")
            for aluno in inadimplentes:
                print(f"👤 Nome: {aluno.nome} | Plano: {aluno.plano.nome}")
            print(f"\n📌  Total de inadimplentes: {len(inadimplentes)}")
        else:
            print("\n👌  Nenhum aluno inadimplente encontrado!")
                

# Sistema para Gerenciamento
class Sistema:
    def __init__(self):
        self._alunos = []

    @property
    def alunos(self):
        return self._alunos

    def adicionar_aluno(self, nome, plano):
        aluno = Aluno(nome, plano)
        self._alunos.append(aluno)
        print(f"Aluno {nome} adicionado com sucesso!")

    def buscar_aluno_por_id(self, aluno_id):
        for aluno in self._alunos:
            if aluno.id == aluno_id:
                return aluno
        print("Aluno não encontrado.")
        return None

    def listar_alunos(self):
        print("\n📋 ----- LISTA DE ALUNOS ----- 📋")
        if not self._alunos:
            print("⚠️  Nenhum aluno cadastrado no sistema.")
        else:
            print(f"\n👥 Total de alunos cadastrados: {len(self._alunos)}")
            for aluno in self._alunos:
                aluno.mostrar_dados()
                #print("-------------------------")
        
    
    @staticmethod
    def selecionar_plano():
        """Menu para selecionar planos predefinidos."""
        planos = {
            "1": Plano("Econômico", 70.0, "3 vezes na semana"),
            "2": Plano("Básico", 100.0, "5 vezes na semana"),
            "3": Plano("Premium", 200.0, "Todos os dias com acompanhamento")
        }
        while True:
            print("\n💼 ----- PLANOS DISPONÍVEIS ----- 💼")
            for key, plano in planos.items():
                print(f"{key}. {plano.nome} - R$ {plano.preco:.2f}: {plano.descricao}")
            print("\nℹ️  Escolha um plano digitando o número correspondente.")
            
            escolha = input("👉 Escolha um plano (1-3): ")
            if escolha in planos:
                print(f"\n✔️  Você selecionou o plano '{planos[escolha].nome}'.")
                return planos[escolha]
            print("\n❌  Opção inválida. Por favor, tente novamente.")
       
        
def menu_principal(sistema):
    """Menu inicial do sistema."""
    while True:
        limpar_terminal()

        print("\n🏠 ----- MENU PRINCIPAL ----- 🏠")
        print("1️⃣  Login como gerente")
        print("2️⃣  Sair")
        print("\nℹ️ Escolha uma opção digitando o número correspondente.\n")

        try:
            opcao = input("👉 Escolha uma opção: ")

            if opcao == "1":
                print("\n🔒 ----- LOGIN DO GERENTE ----- 🔒")
                usuario = input("👤  Digite o nome de usuário: ")
                senha = input("🔑 Digite a senha: ")
                gerente = Gerente(usuario, "Administrador")
                if gerente.autenticar(usuario, senha):
                    print("\n✔️  Acesso autorizado! Bem-vindo ao sistema, gerente!")
                    input("👉 Pressione Enter para acessar o menu do gerente...")
                    menu_gerente(sistema, gerente)
                else:
                    print("\n❌ Credenciais inválidas. Por favor, tente novamente.")
                    input("👉 Pressione Enter para retornar ao menu principal...")
            elif opcao == "2":
                print("\n🚪 Saindo do sistema. Até logo! 👋")
                break
            else:
                print("\n⚠️  Opção inválida. Por favor, escolha uma das opções disponíveis.")
                input("👉 Pressione Enter para continuar...")

        except Exception as e:
            print(f"\n❌ Ocorreu um erro inesperado: {e}")
            print("⚠️ Por favor, tente novamente ou contate o suporte.")
            input("👉 Pressione Enter para continuar...")


def menu_gerente(sistema, gerente):
    """Menu principal para gerenciamento do sistema pelo gerente."""
    while True:
        limpar_terminal()
        print("\n🧑‍💼 ----- MENU DO GERENTE ----- 🧑‍💼")
        print("1️⃣  Listar alunos")
        print("2️⃣  Registrar frequência do dia")
        print("3️⃣  Adicionar aluno")
        print("4️⃣  Buscar aluno pelo nome")
        print("5️⃣  Gerar relatório de inadimplentes")
        print("6️⃣  Mostrar alunos com pagamento em dia")
        print("7️⃣  Cadastrar novo gerente")
        print("8️⃣  Sair")
        print("\nℹ️  Escolha uma opção digitando o número correspondente.\n")

        opcao = input("👉 Escolha uma opção: ")

        if opcao == "1":
            #print("\n📋 ----- LISTA DE ALUNOS ----- 📋")
            gerente.listar_alunos(sistema)
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "2":
            print("\n🕒 ----- REGISTRAR FREQUÊNCIA ----- 🕒")
            aluno_id = input("Digite o ID do aluno: ")
            gerente.registrar_frequencia(sistema, aluno_id)
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "3":
            print("\n✏️ ----- CADASTRAR NOVO ALUNO ----- ✏️")
            nome = input("Digite o nome do aluno: ")
            plano = Sistema.selecionar_plano()
            if plano:
                sistema.adicionar_aluno(nome, plano)
                print(f"\n✔️  Aluno '{nome}' cadastrado com sucesso no plano '{plano.nome}'!")
            else:
                print("\n❌  Plano inválido. Tente novamente.")
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "4":
            print("\n🔍 ----- BUSCAR ALUNO ----- 🔍")
            termo = input("Digite o nome ou parte do nome do aluno (ou pressione Enter para listar todos): ").lower()
            if not termo:
                resultados = sorted(sistema.alunos, key=lambda x: x.nome)
            else:
                resultados = sorted([a for a in sistema.alunos if termo in a.nome.lower()], key=lambda x: x.nome)

            if resultados:
                print("\n👥 ----- ALUNOS ENCONTRADOS ----- 👥")
                for aluno in resultados:
                    print(f"📌 ID: {aluno.id} - Nome: {aluno.nome}")
                aluno_id = input("👉 Digite o ID do aluno para selecionar ou 0 para voltar: ")
                if aluno_id == "0":
                    print("\n↩️  Voltando ao menu do gerente...")
                else:
                    aluno_selecionado = sistema.buscar_aluno_por_id(aluno_id)
                    if aluno_selecionado:
                        menu_aluno(aluno_selecionado)
                    else:
                        print("\n❌  ID inválido. Tente novamente.")
            else:
                print("\n⚠️ Nenhum aluno encontrado com o termo informado.")
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "5":
            print("\n📊 ----- RELATÓRIO DE INADIMPLENTES ----- 📊")
            Relatorio.gerar_relatorio_inadimplentes(sistema)
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "6":
            print("\n✅ ----- ALUNOS COM PAGAMENTO EM DIA ----- ✅")
            pagamentos_em_dia = [
                aluno for aluno in sistema.alunos
                if not aluno.pagamento.verificar_inadimplencia()
            ]
            if pagamentos_em_dia:
                for aluno in pagamentos_em_dia:
                    ultimo_pagamento = aluno.pagamento.historico[-1]["data"]
                    print(f"📌  ID: {aluno.id} - Nome: {aluno.nome} - Plano: {aluno.plano.nome} - Último pagamento: {ultimo_pagamento.strftime('%d/%m/%Y')}")
            else:
                print("\n🎉 Nenhum aluno com pagamentos pendentes!")
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "7":
            print("\n👤 ----- CADASTRAR NOVO GERENTE ----- 👤")
            gerente.cadastrar_gerente()
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "8":
            print("\n🚪 Saindo do menu do gerente. Até logo! 👋")
            break

        else:
            print("\n⚠️  Opção inválida. Por favor, tente novamente.")
            input("\n👉 Pressione Enter para continuar...")
            

def menu_aluno(aluno):
    """Menu para gerenciamento individual do aluno."""
    while True:
        limpar_terminal()  # Limpa o terminal antes de exibir o menu do aluno
        print(f"\n🏋️ ----- MENU DO ALUNO: {aluno.nome} ----- 🏋️")
        print("1️⃣  Mudar de plano")
        print("2️⃣  Cancelar matrícula")
        print("3️⃣  Reativar matrícula")
        print("4️⃣  Exibir histórico de pagamentos")
        print("5️⃣  Registrar pagamento")
        print("6️⃣  Exibir relatório de frequência")
        print("7️⃣  Voltar")
        print("\nℹ️  Escolha uma opção digitando o número correspondente.\n")

        opcao = input("👉 Escolha uma opção: ")

        if opcao == "1":
            print("\n📋 ----- MUDAR DE PLANO ----- 📋")
            novo_plano = Sistema.selecionar_plano()
            if novo_plano:
                aluno.plano = novo_plano
                print(f"\n✔️  Plano alterado para '{novo_plano.nome}' com sucesso!")
            else:
                print("\n❌ Plano inválido. Tente novamente.")
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "2":
            print("\n🚫 ----- CANCELAR MATRÍCULA ----- 🚫")
            aluno.cancelar_matricula()
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "3":
            print("\n🔄 ----- REATIVAR MATRÍCULA ----- 🔄")
            aluno.reativar_matricula()
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "4":
            print("\n💳 ----- HISTÓRICO DE PAGAMENTOS ----- 💳")
            aluno.pagamento.exibir_historico()
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "5":
            print("\n💰 ----- REGISTRAR PAGAMENTO ----- 💰")
            while True:
                try:
                    valor = float(input(f"Digite o valor do pagamento para o plano '{aluno.plano.nome}' (R$ {aluno.plano.preco:.2f}): R$ "))
                    if valor > 0:
                        if aluno.pagamento.registrar_pagamento(valor, aluno.plano.preco):
                            print("\n✔️  Pagamento registrado com sucesso!")
                            break  # Sai do loop após o registro bem-sucedido
                        else:
                            print("\n❌ Pagamento não registrado. Verifique os detalhes e tente novamente.")
                    else:
                        print("\n⚠️  O valor deve ser positivo.")
                except ValueError:
                    print("\n⚠️  Entrada inválida. Digite um número.")

                # Adicionar uma opção para sair do loop
                sair = input("❓ Deseja tentar novamente? (S/N): ").strip().lower()
                if sair == 'n':
                    print("\n↩️  Cancelando registro de pagamento.")
                    break
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "6":
            print("\n🕒 ----- RELATÓRIO DE FREQUÊNCIA ----- 🕒")
            aluno.frequencia.exibir_frequencia()
            input("\n👉 Pressione Enter para continuar...")

        elif opcao == "7":
            print("\n↩️  Voltando ao menu do gerente...")
            break

        else:
            print("\n⚠️  Opção inválida. Por favor, escolha uma das opções disponíveis.")
            input("\n👉 Pressione Enter para continuar...")


def limpar_terminal():
    # Verifica o sistema operacional
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")  # Comando para limpar o terminal no Windows
    else:
        os.system("clear")  # Comando para limpar o terminal em sistemas Unix (Linux/Mac)

if __name__ == "__main__":
    sistema = Sistema()

    # Criando gerente inicial
    gerente_inicial = Gerente("admin", "Administrador")
    Gerente._credenciais["admin"] = "senha123"

    # Planos disponíveis
    plano_economico = Plano("Econômico", 70.0, "3 vezes na semana")
    plano_basico = Plano("Básico", 100.0, "5 vezes na semana")
    plano_premium = Plano("Premium", 200.0, "Todos os dias com acompanhamento")

    # Adicionando 10 alunos com planos variados
    sistema.adicionar_aluno("João Silva", plano_economico)
    sistema.adicionar_aluno("Maria Oliveira", plano_basico)
    sistema.adicionar_aluno("Pedro Santos", plano_premium)
    sistema.adicionar_aluno("Ana Souza", plano_basico)
    sistema.adicionar_aluno("Carlos Lima", plano_economico)
    sistema.adicionar_aluno("Fernanda Costa", plano_premium)
    sistema.adicionar_aluno("Juliana Ribeiro", plano_basico)
    sistema.adicionar_aluno("Gustavo Almeida", plano_premium)
    sistema.adicionar_aluno("Mariana Rocha", plano_economico)
    sistema.adicionar_aluno("Rafael Fernandes", plano_basico)
    
    # Mensagem de inicialização
    limpar_terminal()
    print("🎉 Bem-vindo ao Sistema de Gestão de Alunos! 🎉")
    print("✅ O sistema está pronto para uso com 10 alunos pré-cadastrados.")
    input("👉 Pressione Enter para acessar o menu principal...")

    # Iniciando o sistema
    menu_principal(sistema)