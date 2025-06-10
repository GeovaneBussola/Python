# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
cédula50 = cédula1 = cédula10 = cédula20 = 0

print('-' * 30)
print('{:^30}'.format('BANCO CEV'))
print('-' * 30)

sacar = int(input('Qual valor deseja sacar? R$'))
if sacar >= 50:
    cédula50 =  sacar // 50
    sacar = sacar % 50
    
if sacar >= 20:
    cédula20 = sacar // 20
    sacar = sacar % 20
    
if sacar >= 10:
    cédula10 = sacar // 10
    sacar = sacar % 10
    
if sacar >= 1:
    cédula1 = sacar
    
    
print('Você receberá')
if cédula50 > 0:print(f'{cédula50} cédula(s) de 50') 
if cédula20 > 0:print(f'{cédula20} cédula(s) de 20')
if cédula10 > 0:print(f'{cédula10} cédula(s) de 10')
if cédula1 > 0:print(f'{cédula1} cédula(s) de 1')


