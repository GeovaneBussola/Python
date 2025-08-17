def lerfloat(msg):
    while True:
        num = input(msg)
        if ',' in num:
            if num.count(',') > 1:
                print('Digito invalido')
                continue
            else:
                num = num.replace(',','.')
        try:
            num = float(num)
            return num
        except:
            print('Digito invalido')
    
def lerint(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except:
            print('Digito ivalido! Porfavor digite um numero valido')

def lerint_intervalo(msg,inicio,fim):
    while True:
        try:
            num = int(input(msg))
            if num >=inicio and num <= fim:
                return num
            else:
        except:
            print('Digito ivalido! Por favor digite um numero valido')
            
def criar_conta(tipo_de_conta):
    print('-'*5,'Criando conta','-'*5)
    titular = str(input('Titular: '))
    saldo = 0
    numero = len(contas) + 1
    if tipo_de_conta == 'normal':
        conta = Conta(titular,saldo,numero)
    elif tipo_de_conta == 'corrente':
        conta = Conta_corrente(titular,saldo,numero)
    contas.append(conta)
    print(f'Conta criada com sucesso!')
    print('-'*25)

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
        print('-'*19)

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

contas = []
print('-='*6,'BANCO','=-'*6)
while True:
    opção = lerint_intervalo('[1] Acessar conta\n[2] Criar conta normal\n[3] Criar conta corrente\n[4] Sair\nOpção: ',1,5)

    #Acessar
    if opção == 1:
        if len(contas) == 0:
            print('Nenhuma conta disponivel')
        else:
            print('-='*5,'Contas Disponiveis','=-'*5) 
            for i in contas:
                print(f'{i.titular} N°{i.numero} Conta {i.tipo_de_conta}')
            opção = lerint('Numero da conta: ') - 1
            if opção >= len(contas) or opção < 0:
                print('Numero de conta inexistente')
            else:
                print('-'*5,f'Bem vindo {contas[opção].titular}!','-'*5)
                while True:
                    escolha_bancaria = lerint_intervalo('[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Sair\nOpção: ',1,4)
                    if escolha_bancaria == 1:
                        contas[opção].depositar()
                    elif escolha_bancaria == 2:
                        contas[opção].sacar()
                    elif escolha_bancaria == 3:
                        contas[opção].extrato()
                    elif escolha_bancaria == 4:
                        print('Saindo da conta...')
                        break

    #Criar conta normal
    elif opção == 2:
        criar_conta('normal')
        
    #Criar conta corrente
    elif opção == 3:
        criar_conta('corrente')
        
    #Sair
    elif opção == 4:
        print('Saindo...')
        break
                    

