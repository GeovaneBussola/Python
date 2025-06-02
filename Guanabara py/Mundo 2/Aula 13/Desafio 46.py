# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Contagem regressiva para fogos de artificio')
print('-' * 43)
sleep(1)
for i in range(10,0,-1):
    print(i)
    sleep(1)
print('KaBOMMMMM')