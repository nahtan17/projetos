import customtkinter
import customtkinter as ctk
from tkinter import messagebox

estoque = []


def cadastrar_produto():
    nome_produto = nometext.get()
    quantidade_produto = quantidadetext.get()

    if nome_produto == '' or quantidade_produto == '':
        messagebox.showerror("Erro, Por favor, preencha todos os campos")
        return
    try:
        quantidade_produto = int(quantidade_produto)
        estoque.append(
            {"nome": nome_produto, "quantidade": quantidade_produto})
        resposta.configure(text="Produto Cadastrado com Sucesso!")
        limpar_campos()
    except ValueError:
        messagebox.showerror("Erro", "Quatidade não pode ser 0")


def limpar_campos():
    nometext.delete(0, ctk.END)
    quantidadetext.delete(0, ctk.END)


def exibir_produtos():
    if not estoque:
        messagebox.showinfo("Nenhum produto cadastrador")
        return
    produtos_lista = ""
    for prod in estoque:
        produtos_lista += f"{prod['nome']} - {prod['quantidade']} unidades\n"
    messagebox.showinfo("Produtos Cadastrados", produtos_lista)


# criar uma janela
janela = customtkinter.CTk()
janela.title("estoque")
janela.geometry("600x380")

# Inserindo Título, sempre pra escrever alguma coisa = Label
cadastro = customtkinter.CTkLabel(janela, text='Cadastro de Produtos')
cadastro.pack(pady=20)  # Fixo o conteúdo

nome = customtkinter.CTkLabel(janela, text='Nome do Produto')  # Label = Nome
nome.pack(pady=5)

nometext = customtkinter.CTkEntry(janela)  # Entry = Inserir Dados no estoque
nometext.pack()

quantidade = customtkinter.CTkLabel(janela, text='Quantidade')  # Label = Nome
quantidade.pack(pady=5)

quantidadetext = customtkinter.CTkEntry(janela)  # Entry = Inserir Dados
quantidadetext.pack()

exibir = customtkinter.CTkButton(
    janela, text='Exibir Produtos:', command=exibir_produtos)
exibir.pack(pady=20)

botao = customtkinter.CTkButton(
    janela, text='Confirmar', command=cadastrar_produto)  # Button = Botão de Clicar
botao.pack(pady=20)

resposta = customtkinter.CTkLabel(janela, text='')
resposta.pack()

janela.mainloop()
