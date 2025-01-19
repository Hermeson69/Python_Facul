from Sistema.sistema import SistemaFarmacia

def testar_sistema_farmacia():
    print("\nIniciando testes do Sistema da Farmácia...\n")
    
    # Inicializar o sistema
    sistema = SistemaFarmacia()
    
    # Testar login com diferentes usuários
    print("\nTeste de Login:")
    sistema.login()  # Digite o CPF válido de um administrador ou outro usuário no teste
    
    # Testar funcionalidades do médico
    print("\nTeste do Menu Médico:")
    sistema.usuario_logado = sistema.usuarios[2]  # Logar como médico
    sistema.menu_medico()
    
    # Testar funcionalidades do enfermeiro
    print("\nTeste do Menu Enfermeiro:")
    sistema.usuario_logado = sistema.usuarios[1]  # Logar como enfermeiro
    sistema.menu_enfermeiro()
    
    # Testar funcionalidades do atendente de farmácia
    print("\nTeste do Menu Atendente de Farmácia:")
    sistema.usuario_logado = sistema.usuarios[3]  # Logar como atendente
    sistema.menu_atendente()
    
    # Testar funcionalidades do guichê
    print("\nTeste do Menu Guichê:")
    sistema.usuario_logado = sistema.usuarios[4]  # Logar como guichê
    sistema.menu_guiche()
    
    # Testar funcionalidades do administrador
    print("\nTeste do Menu Administrador:")
    sistema.usuario_logado = sistema.usuarios[5]  # Logar como administrador
    sistema.menu_administrador()
    
    # Testar manipulação de estoque
    print("\nTeste de Estoque de Medicamentos:")
    atendente = sistema.usuarios[3]
    atendente.adicionar_medicamento("Ibuprofeno", 30)
    print(atendente.verificar_estoque("Ibuprofeno")[1])
    
    # Testar registro e consulta de pacientes
    print("\nTeste de Registro e Consulta de Pacientes:")
    sistema.guiche.registrar_paciente("Maria", "22233344455", 30)
    sistema.usuario_logado = sistema.usuarios[2]  # Logar como médico
    sistema.usuario_logado.realizar_consulta(sistema, "22233344455", "Ibuprofeno", 10)
    
    # Testar relatórios do administrador
    print("\nTeste de Relatórios do Administrador:")
    sistema.usuario_logado = sistema.usuarios[5]  # Logar como administrador
    sistema.usuario_logado.movimentacoes_do_sistema()
    
    print("\nTodos os testes foram executados com sucesso.\n")

if __name__ == "__main__":
    testar_sistema_farmacia()
