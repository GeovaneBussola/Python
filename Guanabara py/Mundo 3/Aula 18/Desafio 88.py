# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogos=[]
print('-=' * 12)
print(f'{"Sorteio Mega Sena":^24}')
print('-=' * 12)
njogos=int(input('Quantos jogos deseja sortear? '))

for i in range(njogos):
    jogos.append(list())
print(f'{"===== Sorteando 10 Jogos =====":^24}')
for i in range(njogos):
    sleep(0.5)
    while len(jogos[i]) < 6:
        aleatorio = randint(1,60)
        if aleatorio not in jogos[i]:
            jogos[i].append(aleatorio)
    jogos[i].sort()
    print(f'Jogo n{i+1}:{jogos[i]}')
print(f'{"=========< Boa Sorte >=========":^30}')


