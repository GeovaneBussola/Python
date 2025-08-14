import tkinter as tk
from tkinter import messagebox

# Lista para armazenar as contas
contas = []

# Classes
class Conta:
    def __init__(self, titular, saldo, numero):
        self.tipo_de_conta = 'Normal'
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def extrato(self):
        return f"Conta {self.tipo_de_conta}\nTitular: {self.titular}\nNúmero: {self.numero}\nSaldo: R${self.saldo:.2f}"

class Conta_corrente(Conta):
    def __init__(self, titular, saldo, numero):
        super().__init__(titular, saldo, numero)
        self.tipo_de_conta = 'Corrente'
        self.limite = 5000

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        return False

    def extrato(self):
        return f"Conta {self.tipo_de_conta}\nTitular: {self.titular}\nNúmero: {self.numero}\nSaldo: R${self.saldo:.2f}\nLimite: R${self.limite:.2f}"

# Funções da interface
def criar_conta(tipo):
    def confirmar():
        nome = entrada_nome.get()
        if nome.strip() == "":
            messagebox.showerror("Erro", "Digite um nome!")
            return
        numero = len(contas) + 1
        if tipo == "normal":
            conta = Conta(nome, 0, numero)
        else:
            conta = Conta_corrente(nome, 0, numero)
        contas.append(conta)
        messagebox.showinfo("Sucesso", f"Conta {tipo} criada!\nNúmero: {numero}")
        janela_criar.destroy()

    janela_criar = tk.Toplevel(janela)
    janela_criar.title(f"Criar Conta {tipo.capitalize()}")

    tk.Label(janela_criar, text="Titular:").pack(pady=5)
    entrada_nome = tk.Entry(janela_criar)
    entrada_nome.pack(pady=5)

    tk.Button(janela_criar, text="Confirmar", command=confirmar).pack(pady=10)

def acessar_conta():
    if not contas:
        messagebox.showwarning("Aviso", "Nenhuma conta criada!")
        return

    janela_acesso = tk.Toplevel(janela)
    janela_acesso.title("Acessar Conta")

    tk.Label(janela_acesso, text="Selecione a conta:").pack(pady=5)
    lista = tk.Listbox(janela_acesso)
    for c in contas:
        lista.insert(tk.END, f"{c.numero} - {c.titular} ({c.tipo_de_conta})")
    lista.pack(pady=5)

    def entrar():
        selecao = lista.curselection()
        if not selecao:
            messagebox.showerror("Erro", "Selecione uma conta!")
            return
        idx = selecao[0]
        conta = contas[idx]
        janela_operacoes(conta)
        janela_acesso.destroy()

    tk.Button(janela_acesso, text="Entrar", command=entrar).pack(pady=5)

def janela_operacoes(conta):
    op_win = tk.Toplevel(janela)
    op_win.title(f"Conta {conta.numero} - {conta.titular}")

    tk.Label(op_win, text=conta.extrato()).pack(pady=5)

    def depositar():
        valor = entrada_valor.get()
        try:
            valor = float(valor.replace(",", "."))
            conta.depositar(valor)
            messagebox.showinfo("Sucesso", "Depósito realizado!")
            op_win.destroy()
            janela_operacoes(conta)
        except:
            messagebox.showerror("Erro", "Valor inválido!")

    def sacar():
        valor = entrada_valor.get()
        try:
            valor = float(valor.replace(",", "."))
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado!")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente!")
            op_win.destroy()
            janela_operacoes(conta)
        except:
            messagebox.showerror("Erro", "Valor inválido!")

    tk.Label(op_win, text="Valor:").pack(pady=5)
    entrada_valor = tk.Entry(op_win)
    entrada_valor.pack(pady=5)

    tk.Button(op_win, text="Depositar", command=depositar).pack(pady=5)
    tk.Button(op_win, text="Sacar", command=sacar).pack(pady=5)
    tk.Button(op_win, text="Extrato", command=lambda: messagebox.showinfo("Extrato", conta.extrato())).pack(pady=5)

# Interface principal
janela = tk.Tk()
janela.title("Banco do Geovane")
janela.geometry("300x250")

tk.Label(janela, text="Banco do Geovane", font=("Arial", 14)).pack(pady=10)

tk.Button(janela, text="Acessar Conta", width=20, command=acessar_conta).pack(pady=5)
tk.Button(janela, text="Criar Conta Normal", width=20, command=lambda: criar_conta("normal")).pack(pady=5)
tk.Button(janela, text="Criar Conta Corrente", width=20, command=lambda: criar_conta("corrente")).pack(pady=5)
tk.Button(janela, text="Sair", width=20, command=janela.quit).pack(pady=5)

janela.mainloop()
