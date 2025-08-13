import tkinter as tk
from tkinter import messagebox, simpledialog

contas = []

# Classes aqui: Conta, Conta_corrente (copie do seu código)
class Conta:
    def __init__(self,titular,saldo,numero):
        self.tipo_de_conta = 'Normal'
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def depositar(self):
        valor_deposito = lerfloat('Valor deposito: R$')
        self.saldo += valor_deposito
        print(f'Deposito de R${valor_deposito:.2f} efetuado com sucesso!!')
        print(f'O novo saldo da sua conta é R${self.saldo:.2f}')
    def sacar(self):
        valor_saque = float(input(f'Saldo disponivel para saque [R${self.saldo}]\nValor saque: R$'))
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            print(f'Saque de R${valor_saque:.2f} efetuado com sucesso!!')
            print(f'O novo saldo da sua conta é R${self.saldo:.2f}')
        else:
            print(f'Você não possui saldo suficiente para realizar este saque!')
    def extrato(self):
        print('-'*5,'Extrato','-'*5)
        print(f'Conta {self.tipo_de_conta}\nTitular {self.titular}\nNumero {self.numero}\nSaldo R${self.saldo}')
    def mostrar_extrato(self):
        print(f'Titiular: R${self.titular}')
        print(f'Numero: R${self.numero}')
        print(f'Saldo: R${self.saldo}')

class Conta_corrente(Conta):
    def __init__(self,titular,saldo,numero):
        super().__init__(titular,saldo,numero)
        self.tipo_de_conta = 'Corrente'
        self.limite = 5000
    def sacar(self):
        valor_saque = float(input(f'Saldo disponivel para saque [limite R${self.limite:.2f} + saldo R${self.saldo:.2f} = R${self.saldo + self.limite:.2f}]\nValor saque: R$'))
        if valor_saque <= self.saldo + self.limite:
            self.saldo -= valor_saque
            print(f'Saque de R${valor_saque:.2f} efetuado com sucesso!!')
            print(f'O novo saldo da sua conta é R${self.saldo:.2f}')
        else:
            print(f'Você não possui saldo suficiente para realizar este saque!')
    def extrato(self):
        print('-'*5,'Extrato','-'*5)
        print(f'Conta-{self.tipo_de_conta}\nTitular {self.titular}\nNumero {self.numero}\nSaldo R${self.saldo:.2f}\nLimite R${self.limite:.2f}')
        print('-'*19)
def criar_conta(tipo):
    nome = simpledialog.askstring("Criar Conta", "Nome do titular:")
    if not nome:
        return
    numero = len(contas) + 1
    if tipo == 'normal':
        conta = Conta(nome, 0, numero)
    else:
        conta = Conta_corrente(nome, 0, numero)
    contas.append(conta)
    messagebox.showinfo("Sucesso", f"Conta {tipo} criada com sucesso!")

def acessar_conta():
    if not contas:
        messagebox.showwarning("Erro", "Nenhuma conta criada ainda.")
        return

    lista = "\n".join([f"{c.numero}: {c.titular} ({c.tipo_de_conta})" for c in contas])
    escolha = simpledialog.askinteger("Acessar Conta", f"Escolha o número da conta:\n{lista}")
    
    conta = next((c for c in contas if c.numero == escolha), None)
    if not conta:
        messagebox.showerror("Erro", "Conta não encontrada.")
        return

    # Menu interno da conta
    while True:
        operacao = simpledialog.askinteger(
            f"Conta de {conta.titular}",
            "[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Voltar"
        )
        if operacao == 1:
            valor = simpledialog.askfloat("Depósito", "Valor a depositar:")
            if valor:
                conta.saldo += valor
                messagebox.showinfo("Depósito", f"Novo saldo: R${conta.saldo:.2f}")
        elif operacao == 2:
            valor = simpledialog.askfloat("Saque", "Valor a sacar:")
            if valor:
                if isinstance(conta, Conta_corrente):
                    total = conta.saldo + conta.limite
                else:
                    total = conta.saldo
                if valor <= total:
                    conta.saldo -= valor
                    messagebox.showinfo("Saque", f"Saque realizado. Novo saldo: R${conta.saldo:.2f}")
                else:
                    messagebox.showwarning("Erro", "Saldo insuficiente.")
        elif operacao == 3:
            msg = f"Titular: {conta.titular}\nNúmero: {conta.numero}\nSaldo: R${conta.saldo:.2f}"
            if isinstance(conta, Conta_corrente):
                msg += f"\nLimite: R${conta.limite:.2f}"
            messagebox.showinfo("Extrato", msg)
        else:
            break

# Criar janela principal
janela = tk.Tk()
janela.title("Banco GUI")
janela.geometry("300x300")

tk.Label(janela, text="Bem-vindo ao Banco!", font=("Arial", 14)).pack(pady=10)

tk.Button(janela, text="Acessar Conta", width=20, command=acessar_conta).pack(pady=5)
tk.Button(janela, text="Criar Conta Normal", width=20, command=lambda: criar_conta("normal")).pack(pady=5)
tk.Button(janela, text="Criar Conta Corrente", width=20, command=lambda: criar_conta("corrente")).pack(pady=5)
tk.Button(janela, text="Sair", width=20, command=janela.quit).pack(pady=20)

janela.mainloop()
