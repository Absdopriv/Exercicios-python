def menu():
    print("\n-- Station Cine --")
    print("1 - Cadastrar filme")
    print("2 - Repor ingressos")
    print("3 - Ver ingressos disponíveis")
    print("4 - Venda de ingressos")
    print("0 - Sair do sistema")
    return input("Escolha uma opção: ")

# Variáveis de controle
ingresso = None
quantidade = 0

while True:
    opcao = menu()
    
    if opcao == "1":
        ingresso = input("Digite o nome do filme: ")
        quantidade = 0
        print(f"Filme '{ingresso}' cadastrado com sucesso!")

    elif opcao == "2":
        if ingresso is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade de ingressos a adicionar: "))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "3":
        if ingresso is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            print(f"Ingresso: {ingresso} | Quantidade em estoque: {quantidade}")

    elif opcao == "4":
        if ingresso is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            retirar = int(input("Digite a quantidade a ser vendida: "))
            if retirar <= 0:
                print("Quantidade deve ser maior que zero!")
            elif retirar > quantidade:
                print("Quantidade insuficiente no estoque!")
            else:
                quantidade -= retirar
                print(f"Vendido {retirar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")