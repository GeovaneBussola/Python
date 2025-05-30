# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite a velocidade do carro em km/h: '))
if velocidade > 80:
    print(f'Você foi multado, o valor da multa é: R${(velocidade-80)*7}')
else:
    print('Sem multa')