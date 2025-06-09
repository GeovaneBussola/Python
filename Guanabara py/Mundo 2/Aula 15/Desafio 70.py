# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = 0
maismil = 0
contador = 0
vlprodutomaisbarato = 0

print('-' * 20)
print('Loja super baratão')
print('-' * 20)

while True:
    continua = ''
    nome = input('Qual é o nome do produto? ')
    valor = float(input('Qual é o valor do produto? '))
    while continua not in ['sim','s','não','nao','n']:
        continua = input('Deseja continuar [S/N]? ').lower().strip()
    total += valor
    maismil+= 1 if valor > 1000 else 0
    if contador == 0:
        nomeprodutomaisbarato = nome
        vlprodutomaisbarato = valor
        contador = 1
    else:
        if vlprodutomaisbarato == valor:
            nomeprodutomaisbarato = nomeprodutomaisbarato + ', ' + nome 
        elif vlprodutomaisbarato > valor:
            nomeprodutomaisbarato = nome
            vlprodutomaisbarato = valor
        
    if continua in ['n','não','nao']:
        break
print(f'{'programa finalizadp':-30^}')
print(f'''O total gasto na compra foi R${total}
{maismil} produtos custam mais de R$1000
{nomeprodutomaisbarato} é o produto mais barato''')
    


