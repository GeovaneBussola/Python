# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
cédula50 = 0
cédula20 = 0
cédula10 = 0
cédula1 = 0
print('-' * 10)
print('Banco CEV')
print('-' * 10)
while True:
    sacar = int(input('qual valor deseja sacar? R$'))
    if sacar > 0:
        break
while True:
    if sacar >= 50:
        sacar-=50
        cédula50+=1
    elif sacar >= 20:
        sacar-=20
        cédula20+=1
    elif sacar >= 10:
        sacar-=10
        cédula10+=1
    elif sacar >= 1:
        sacar-=1
        cédula1+=1
    else:
        break
print('Você receberá')
if cédula50 > 0:print(f'{cédula50} cédula(s) de 50') 
if cédula20 > 0:print(f'{cédula20} cédula(s) de 20')
if cédula10 > 0:print(f'{cédula10} cédula(s) de 10')
if cédula1 > 0:print(f'{cédula1} cédula(s) de 1')


