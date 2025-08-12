def lerfloat(msg):
    num = input(msg)
    if ',' in num:
        if num.count(',') > 1:
            return 'Digito invalido'
        else:
            num = num.replace(',','.')
    try:
        num = float(num)
        return num
    except:
        return 'Digito invalido'

class Conta:
    def __init__(self,titular,saldo,numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
    def depositar(self):
        valor_deposito = float(input('Valor deposito: R$'))
        self.saldo += valor_deposito
    def sacar(self):
        valor_saque = float(input(f'Saldo disponivel para saque [R${self.saldo}]\nValor saque: R$'))
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            print(f'Saque de R${valor_saque:.2f} efetuado com sucesso!!')
            print(f'O novo saldo da sua conta é R${self.saldo:.2f}')
        else:
            print(f'Você não possui saldo suficiente para realizar este saque!')
    def mostrar_extrato(self):
        print(f'Titiular:{self.titular}')
        print(f'Numero:{self.numero}')
        print(f'Saldo:{self.saldo}')


ct1 = Conta('Geovane',0,122)

while True:
    msg = lerfloat('Digite o numero float: ')
    print(msg)
    escolha = int(input('Escolha: '))
    if escolha == 1:
        ct1.depositar()
    elif escolha == 2:
        ct1.sacar()
    elif escolha == 3:
        ct1.mostrar_extrato()