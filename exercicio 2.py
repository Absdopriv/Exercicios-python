# Lista para armazenar os pacientes
pacientes = []

# Função para cadastrar um novo paciente
def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "telefone": telefone
    }

    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!\n")

# Função para listar todos os pacientes
def listar_pacientes():
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    for i, paciente in enumerate(pacientes):
        print(f"{i+1}. Nome: {paciente['nome']}, Idade: {paciente['idade']}, CPF: {paciente['cpf']}, Telefone: {paciente['telefone']}")
    print()

# Função para atender o primeiro paciente da fila
def atender_paciente():
    print("\n--- Atender Paciente ---")
    if not pacientes:
        print("Nenhum paciente na fila para atendimento.\n")
        return

    paciente = pacientes.pop(0)
    print(f"Atendendo paciente: {paciente['nome']} (CPF: {paciente['cpf']})\n")

# Menu principal
def menu():
    while True:
        print("===== Sistema de Cadastro de Pacientes =====")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Atender paciente")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            atender_paciente()
        elif opcao == "4":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Iniciar o sistema
menu()