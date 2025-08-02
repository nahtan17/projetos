estoque = []


def cadastrar_produto():
    nome_produto = nometext.get()
    quantidade_produto = quantidadetext.get()

    if nome_produto == "" or quantidade_produto == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    # Adicionando produto à lista de estoque
    try:
        quantidade_produto = int(quantidade_produto)
        estoque.append({"nome": nome_produto, "quantidade": quantidade_produto})
        resposta.configure(text="Produto Cadastrado com Sucesso!")
        limpar_campos()
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro.")

# Função para limpar os campos


def limpar_campos():
    nometext.delete(0, ctk.END)
    quantidadetext.delete(0, ctk.END)

# Função para exibir os produtos cadastrados


def exibir_produtos():
    if not estoque:
        messagebox.showinfo("Estoque", "Nenhum produto cadastrado.")
        return

    produtos = "\n".join(
        [f"{prod['nome']} - {prod['quantidade']} unidades" for prod in estoque])
    messagebox.showinfo("Produtos Cadastrados", produtos)