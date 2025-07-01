# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
dicionario={}

for i in range(1,5):
    dicionario[f'Jogador {i}'] = randint(1,6)
for k,i in dicionario.items():
    print(f'{k} tirou: {i} no dado')
    sleep(1)
ranking = sorted(dicionario.items(),key=itemgetter(1),reverse=True)
print(30*'-')
for k,i in enumerate(ranking):
    print(f'{k+1}° lugar: {i[0]} com {i[1]}')
