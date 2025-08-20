#Exercício 1
#Sistema de estoque
def menu():
    print("/n--- sistema de Estoque ---")
    print("1 - Cadastra protudo")
    print("2 - Retirar do estoque")
    print("3- Adicionar ao  estoque")
    print("4 - Ver quantidade em estoque")
    print("0 - Sair")
    return input("Escolha uma opção: ")
    
    
#Vairáveis de controle
produto = None
quantidade = 0

while True:
    opcao = menu()

    if opcao =="1":
        produto = input("Digite o nome do produto: ")
        quantidade = 0
        print(f"produto '{produto}' cadastrado com sucesso!")
        
    elif opcao == "2":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            retirar = int(input("Digite a quantidade a retirar: "))
            if retirar <=0:
                print("A quantidade deve ser maior que zero!")
            elif retirar > quantidade:
                print("Quantidade insulficiente no estoque!")
            else:
                quantidade -= retirar
                print(f"Retirado {retirar} unidade(s). estoque atual: {quantidade}")
                
    elif opcao == "3":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar:"))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade(s). Estoque atual: {quantidade}")
                
    elif opcao == "4":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            print(f"produto: {produto} quantido em estoque: {quantidade}")
        
    elif opcao == "0":
        print("Saindo do sistema... até mais!")
        break
    else:
        print("Opção invalida! tente novamente.") **


diagrama
---
config:
  theme: redux
---
flowchart TD
    A(["Inicio"]) --> B["Menu"]
    B --> C["Qual a Opção"]
    C --> n1["1 - Cadastra protudo"] & n3["2 - Retirar do estoque"] & n8["3- Adicionar ao estoque"] & n13["4 - Ver quantidade em estoque"]
    n1 --> n2["Digite o nome do produto"]
    n2 --> n4["cadastrado com sucesso"]
    n3 --> n5["Digite a quantidade a retirar"]
    n5 --> n6["A quantidade deve ser maior que zero"]
    n6 --> n9["Quantidade insulficiente no estoque!"]
    n8 --> n10["Digite a quantidade a adicionar"]
    n10 --> n11["A quantidade deve ser maior que zero"]
    n11 --> n12["Adicionado unidade(s). Estoque atual:"]
    n13 --> n14["mostra a quantidade do produto cadastrado"]
    n4 --> n16["Volte ao menu"]
    n9 --> n17["Volte ao menu"]
    n12 --> n18["Volte ao menu"]
    n14 --> n19["Volte ao menu"]
    n18 --> n20["Menu"]
    n17 --> n20
    n16 --> n20
    n19 --> n20
    n15["Rectangle"]
    C@{ shape: diam}
    n5@{ shape: rect}
    n6@{ shape: diam}
    n11@{ shape: diam}
    n15@{ shape: rect}