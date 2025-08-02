import customtkinter
import customtkinter as ctk
from tkinter import messagebox
import json


estoque = []


def salvar_dados():
    with open("estoque.json", "w") as f:
        json.dump(estoque, f)


def carregar_dados():
    try:
        with open("estoque.json", "r") as f:
            global estoque
            estoque = json.load(f)
    except FileNotFoundError:
        estoque = []


def cadastrar_produtos():
    nome_produto = nometext.get()
    quantidade_produto = quantidadetext.get()

    if nome_produto == "" or quantidade_produto == "":
        messagebox.showinfo("ERRO, Preencha todos os campos")
        return

    try:
        quantidade_produto = int(quantidade_produto)
        estoque.append(
            {"nome": nome_produto, "quantidade": quantidade_produto})
        resposta.configure(text="Produto Cadastrado com Sucesso!")
        salvar_dados()
        limpar_campos()
    except ValueError:
        messagebox.showerror("Erro, A Quantidade não pode ser 0")


def remover_produto():
    nome_produto = nometext.get()

    if nome_produto == "":
        messagebox.showinfo("Erro, insira o nome do produto")
        return

    produto_encontrado = False
    for prod in estoque:
        if prod["nome"].lower() == nome_produto.lower():
            estoque.remove(prod)
            produto_encontrado = True
            break

    if produto_encontrado:
        resposta.configure(text="Produto Removido com Sucesso!")
        salvar_dados()
        limpar_campos()
    else:
        messagebox.showinfo("Produto não encontrado no estoque")


def adicionar_quantidade():
    nome_produto = nometext.get()
    quantidade_produto = quantidadetext.get()

    if nome_produto == "" or quantidade_produto == "":
        messagebox.showinfo("Erro, Preencha todos os campos")
        return

    try:
        quantidade = int(quantidade_produto)
        produto_encontrado = False

        for prod in estoque:
            if prod["nome"].lower() == nome_produto.lower():
                prod["quantidade"] += quantidade
                produto_encontrado = True
                break

        if produto_encontrado:
            resposta.configure(text="Quantidade Adicionada com Sucesso!")
            salvar_dados()
            limpar_campos()
        else:
            messagebox.showinfo("Produto não encontrado no estoque")
    except ValueError:
        messagebox.showerror(
            "Erro, A quantidade precisa ser um número inteiro")


def limpar_campos():
    nometext.delete(0, ctk.END)
    quantidadetext.delete(0, ctk.END)


def exibir_produto():
    if not estoque:
        messagebox.showinfo("Nenhum Produto Cadastrado")
        return
    produto_listas = ""
    for prod in estoque:
        produto_listas += f"{prod["nome"]} - {prod["quantidade"]} unidades\n"
    messagebox.showinfo("Produto Cadastrado", produto_listas)


janela = customtkinter.CTk()
janela.title("Estoque")
janela.geometry("680x380")

carregar_dados()

cadastro = customtkinter.CTkLabel(janela, text="Cadastrar Produto")
cadastro.pack(pady=10)

nome = customtkinter.CTkLabel(janela, text="Nome do Produto")
nome.pack(pady=5)

nometext = customtkinter.CTkEntry(janela)
nometext.pack()

quantidade = customtkinter.CTkLabel(janela, text="Quantidade")
quantidade.pack()

quantidadetext = customtkinter.CTkEntry(janela)
quantidadetext.pack()

botao = customtkinter.CTkButton(
    janela, text="Adicionar Produto", command=cadastrar_produtos)
botao.pack(pady=10)

adicionar_quantidade_botao = customtkinter.CTkButton(
    janela, text="Adicionar Quantidade", command=adicionar_quantidade)
adicionar_quantidade_botao.pack(pady=10)

remover = customtkinter.CTkButton(
    janela, text="Remover Produto", command=remover_produto)
remover.pack(pady=5)

exibir = customtkinter.CTkButton(
    janela, text="Exibir Produtos", command=exibir_produto)
exibir.pack(pady=5)


resposta = customtkinter.CTkLabel(janela, text="")
resposta.pack()

janela.mainloop()
