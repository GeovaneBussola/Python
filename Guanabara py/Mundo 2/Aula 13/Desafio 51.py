# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
resultado=0
primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
for i in range(10):
    print(f'{primeiro_termo}, ' ,end='')
    primeiro_termo += razão
print('Acabou')