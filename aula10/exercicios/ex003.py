# 3- Faça um programa em Python que solicite ao usuário a placa e o valor da multa de 15
# carros. As informações obtidas devem ser armazenadas em 2 listas distintas (observe que
# cada lista poderá ter apenas 15 itens armazenados e que na posição i das duas listas
# ficarão armazenados: a placa i e o valor de venda i, veja exemplo abaixo).
# 0 AAA-1234
# 1 CCC-1234
# 2 AAA-1234
# 3 DDD-1234
# ...
# 14 BBB-1234
# 0 880.41
# 1 1467.35
# 2 293.47
# 3 293.47
# ...
# 14 2934.70
# É obrigatório o uso de estrutura de repetição e listas.
# Calcule e mostre e o valor médio de todas as multas e
# quantos carros possuem o valor de multa maior ou
# igual a R$300.00, para isso utilize os dados
# armazenados nas listas descritas anteriormente e
# estrutura de repetição.

placas=[]
multas=[]
contador=0
print('Digite as 15 placas:')
for i in range(1,16):
    placas.append(input(f'{i}° placa: '))
print('Digite o valor da multa de cada placa:')
for i in range(1,16):
    multas.append(float(input(f'[placa {placas[i]}] Multa: ')))
media_multas = sum(multas) / len(multas)
for i in multas:
    if i >= 300:
        contador+=1
print(f'O valor médio das multas é R${media_multas:.2f}')
print(f'{contador} placas possuem valor igual ou superior a R$300,00')

        
        
