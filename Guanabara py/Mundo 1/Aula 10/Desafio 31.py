# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = int(input('Digite a distancia da viagem em km/h: '))
if viagem <= 200:
    print(f'O valor da passagem é R${viagem * 0.50:.2f}')
else:
    print(f'O valor da passagem é R${viagem * 0.45:.2f}')
