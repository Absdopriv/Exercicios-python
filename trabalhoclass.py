#cadastra novo email
class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"Email: {self.email}"

#sistema de usuario
class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self):
        print("\n--- Cadastro de Usuário ---")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")

        # Verificar se já existe o email
        for usuario in self.usuarios:
            if usuario.email == email:
                print("Erro: Email já cadastrado!\n")
                return

        novo_usuario = Usuario(email, senha)
        self.usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso!\n")

    def listar_usuarios(self):
        print("\n--- Lista de Usuários ---")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.\n")
            return

        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. {usuario}")
        print()

    def buscar_usuario(self):
        print("\n--- Buscar Usuário ---")
        email = input("Digite o email para buscar: ")

        for usuario in self.usuarios:
            if usuario.email == email:
                print(f"Usuário encontrado: {usuario}\n")
                return
        print("Usuário não encontrado.\n")
#login
    def login(self):
        print("\n--- Login ---")
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")

        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha:
                print(f"Login realizado com sucesso! Bem-vindo {usuario.email}\n")
                return
        print("Email ou senha incorretos.\n")
#menu
    def menu(self):
        while True:
            print("===== Sistema de Usuários =====")
            print("1. Cadastrar usuário")
            print("2. Listar usuários")
            print("3. Buscar usuário")
            print("4. Fazer login")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_usuario()
            elif opcao == "2":
                self.listar_usuarios()
            elif opcao == "3":
                self.buscar_usuario()
            elif opcao == "4":
                self.login()
            elif opcao == "5":
                print("Saindo do sistema. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.\n")

# Iniciar o sistema
sistema = SistemaUsuarios()
sistema.menu()