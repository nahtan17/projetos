estoque = []


def cadastrar_produto():
    nome = input('Digite o nome do Produto: ')
    quantidade = int(input('Digite a quantidade: '))
    produto = {"nome": nome, "quantidade": quantidade}
    estoque.append(produto)
    print('Produto Cadastrado com Sucesso')


def adicionar_produto():
    nome = input('Digite o Produto que queira adicionar: ')
    quantidade_adicional = input('Digite a quantidade: ')

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            produto["quantidade"] += quantidade_adicional
            print(
                f"O Produto {nome} foi adicionado ao Estoque, sua Quantidade atual é {quantidade_adicional}")
            return
    print('Produto não encontrado: {nome}')


def remover_produto():
    nome = input('Digite o Produto que queira remover: ')
    quantidade_remover = input('Digite a quantidade: ')

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            produto["quantidade"] -= quantidade_remover
            print(f"O Produto {nome} foi removido do estoque")
        else:
            print("Produto não encontrado {nome}")


def exibir_estoque():
    if len(estoque) == 0:
        print('Estoque Vazio')
    else:
        print("\n --- Estoque Atual ---")
        for produto in estoque:
            print(
                f"\nProduto: {produto["nome"]} | Quatidade: {produto["quantidade"]}\n")


def menu():
    while True:
        print("Sistema de Controle de Estoque")
        print("1. Cadastrar Produto")
        print("2. Adicionar Produto")
        print("3. Remover Produto")
        print("4. Exibir Estoque")
        print("5. Sair")

        opcao = input('Digite uma opcao (1-5): ')

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            adicionar_produto()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            exibir_estoque()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Digite uma opção válida")


menu()
