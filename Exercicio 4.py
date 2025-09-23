from dataclasses import dataclass
from datetime import datetime
#importando informações do banco de dados
@dataclass
class Publicacao:
    conteudo: str
    descricao: str
    autor: str
    data_hora: datetime
    curtidas: int = 0

lista_publicacoes = []
#criando uma classe da publicação e uma lista referente a classe
def criar_publicacao():
    print("\n=== CRIAR PUBLICAÇÃO ===")
    conteudo = input("Digite o conteúdo da publicação: ")
    descricao = input("Digite a descrição: ")
    autor = input("Digite o nome do autor: ")
    data_hora = datetime.now()
    nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
    lista_publicacoes.append(nova_publicacao)
    print("Publicação criada com sucesso!")
#criando a função criar publicação "inputando strings" aos valores
def curtir_publicacao():
    print("\n=== CURTIR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação para curtir: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            pub = lista_publicacoes[indice]
            pub.curtidas += 1
            print("Publicação curtida!")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")
#criei a função curtir a publicação e a informação de erro prescrito
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
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")
# criei a função de vizualização única, erro prescrito e printei na tela informações da publicação.
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
#criei a função de ver e pequisar o perfil do autor de publicação, ja indicando se caso tiver 0 publicações do autor apareça uma mensagem pré escolhida
def visualizar_feed():
    print("\n=== FEED ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    for i, pub in enumerate(lista_publicacoes, 1):
        print(f"[{i}]. {pub.autor} - {pub.curtidas} curtidas")
        print(f"  {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print(f"  {pub.conteudo}")
        print(f"  {pub.descricao}")
        print("- " * 40)
# criei função de vizualizar o feed, pré setando uma mensagem caso não tebha publicações disponíveis e criei organização das postagems por número. 
def menu():
    while True:
        print("\n=== REDE SOCIAL ===")
        print("1. Criar Publicação")
        print("2. Curtir Publicação")
        print("3. Visualizar Feed")
        print("4. Visualizar Publicação Individual")
        print("5. Visualizar Publicações por Autor")
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
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
        if input("\nDeseja continuar? (s/n): ").lower() != "s":
            break
#Criei a função do menu, printando na tela as opções das funções e os casos relacionados à eles
if __name__ == "__main__":
    menu()
# O nome é igual ao "main" é a mesma informação e encerrei o menu.
