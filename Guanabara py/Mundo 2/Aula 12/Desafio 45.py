# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import time
from random import randint
while True:
    itens = ('pedra','papel','tesoura')
    computador = randint(0,2)
    print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')

    jogador = int(input('Qual é sua jogada? '))
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PÔ')

    print('-' *20)
    print(f'\033[31mComputador = {itens[computador]}\n\033[32mJogador = {itens[jogador]}\033[m')
    print('-' *20)
    if computador == 0:
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('\033[32mJogador venceu\033[m')
        elif jogador == 2:
            print('\033[31mComputador venceu\033[m')
        else:
            print('Jogada invalida')
    elif computador == 1:
        if jogador == 0:
            print('\033[31mComputador venceu\033[m')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('\033[32mJogador venceu\033[m')
        else:
            print('Jogada invalida')
    else:
        if jogador == 0:
            print('\033[32mJogador venceu\033[m')
        elif jogador == 1:
            print('\033[31mComputador venceu\033[m')
        elif jogador == 2:
            print('Empate')
        else:
            print('Jogada invalida')
