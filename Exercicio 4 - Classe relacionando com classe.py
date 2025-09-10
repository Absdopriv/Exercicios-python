from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Usuario:
    nome: str
    email: str
    senha: str  # Novo campo para senha

@dataclass
class Comentario:
    autor: str
    texto: str
    data_hora: datetime

@dataclass
class Publicacao:
    conteudo: str
    descricao: str
    autor: str
    data_hora: datetime
    curtidas: int = 0
    comentarios: list = field(default_factory=list)

lista_usuarios = []
lista_publicacoes = []

def cadastrar_usuario():
    print("\n=== CADASTRAR USUÁRIO ===")
    nome = input("Digite o nome de usuário: ")
    email = input("Digite o email: ")
    senha = input("Digite a senha (mínimo 6 caracteres): ")
    
    # Validação da senha
    if len(senha) < 6:
        print("A senha deve ter pelo menos 6 caracteres.")
        return None
    
    if any(u.nome == nome for u in lista_usuarios):
        print("Usuário já existe.")
        return None
    
    usuario = Usuario(nome, email, senha)
    lista_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario

def verificar_senha(autor, senha):
    """Verifica se a senha está correta para o usuário."""
    for usuario in lista_usuarios:
        if usuario.nome == autor and usuario.senha == senha:
            return True
    return False

def criar_publicacao():
    print("\n=== CRIAR PUBLICAÇÃO ===")
    if not lista_usuarios:
        print("Nenhum usuário cadastrado. Cadastre-se primeiro.")
        return
    autor = input("Digite o nome do autor: ")
    if not any(u.nome == autor for u in lista_usuarios):
        print("Usuário não cadastrado.")
        return
    
    # Verificar senha antes de criar publicação
    senha = input("Digite sua senha: ")
    if not verificar_senha(autor, senha):
        print("Senha incorreta.")
        return
    
    conteudo = input("Digite o conteúdo da publicação: ")
    descricao = input("Digite a descrição: ")
    data_hora = datetime.now()
    nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
    lista_publicacoes.append(nova_publicacao)
    print("Publicação criada com sucesso!")

def curtir_publicacao():
    print("\n=== CURTIR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação para curtir: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            autor = input("Digite seu nome de usuário: ")
            if not any(u.nome == autor for u in lista_usuarios):
                print("Usuário não cadastrado.")
                return
            # Verificar senha antes de curtir
            senha = input("Digite sua senha: ")
            if not verificar_senha(autor, senha):
                print("Senha incorreta.")
                return
            pub = lista_publicacoes[indice]
            pub.curtidas += 1
            print("Publicação curtida!")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")

def comentar_publicacao():
    print("\n=== COMENTAR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação para comentar: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            autor = input("Digite seu nome de usuário: ")
            if not any(u.nome == autor for u in lista_usuarios):
                print("Usuário não cadastrado.")
                return
            # Verificar senha antes de comentar
            senha = input("Digite sua senha: ")
            if not verificar_senha(autor, senha):
                print("Senha incorreta.")
                return
            texto = input("Digite o comentário: ")
            data_hora = datetime.now()
            comentario = Comentario(autor, texto, data_hora)
            pub = lista_publicacoes[indice]
            pub.comentarios.append(comentario)
            print("Comentário adicionado!")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")

def visualizar_publicacao_individual():
    print("\n=== VISUALIZAR PUBLICAÇÃO INDIVIDUAL ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            pub = lista_publicacoes[indice]
            print(f"Autor: {pub.autor}")
            print(f"Data: {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
            print(f"Conteúdo: {pub.conteudo}")
            print(f"Descrição: {pub.descricao}")
            print(f"Curtidas: {pub.curtidas}")
            print("Comentários:")
            if not pub.comentarios:
                print("Nenhum comentário.")
            for com in pub.comentarios:
                print(f"- {com.autor} ({com.data_hora.strftime('%d/%m/%Y %H:%M')}): {com.texto}")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")

def visualizar_publicacoes_por_autor():
    print("\n=== PUBLICAÇÕES POR AUTOR ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    autor = input("Digite o nome do autor: ")
    publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower()]
    if not publicacoes_autor:
        print(f"Nenhuma publicação encontrada para {autor}.")
        return
    for pub in publicacoes_autor:
        print(f"- {pub.conteudo} ({pub.curtidas} curtidas)")

def visualizar_feed():
    print("\n=== FEED ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    for i, pub in enumerate(lista_publicacoes, 1):
        print(f"[{i}]. {pub.autor} - {pub.curtidas} curtidas - {len(pub.comentarios)} comentários")
        print(f"  {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print(f"  {pub.conteudo}")
        print(f"  {pub.descricao}")
        print("- " * 40)

def menu():
    if not lista_usuarios:
        print("\n=== CADASTRO OBRIGATÓRIO ===")
        cadastrar_usuario()
    while True:
        print("\n=== REDE SOCIAL ===")
        print("1. Criar Publicação")
        print("2. Curtir Publicação")
        print("3. Visualizar Feed")
        print("4. Visualizar Publicação Individual")
        print("5. Visualizar Publicações por Autor")
        print("6. Cadastrar Novo Usuário")
        print("7. Comentar Publicação")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_publicacao()
        elif opcao == "2":
            curtir_publicacao()
        elif opcao == "3":
            visualizar_feed()
        elif opcao == "4":
            visualizar_publicacao_individual()
        elif opcao == "5":
            visualizar_publicacoes_por_autor()
        elif opcao == "6":
            cadastrar_usuario()
        elif opcao == "7":
            comentar_publicacao()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
        if input("\nDeseja continuar? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    menu()
