# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
import time

numero = randint(0,5)
tentativa = int(input('Tente acertar o numero sorteado de 0 a 5: '))
time.sleep(2)
print('Você acertou!' if tentativa == numero else 'Você perdeu!')
print(f'Eu pensei no numero {numero}')
