# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maioridade = 0
menoridade = 0
for i in range(1,8):
    anos =date.today().year - int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    if anos > 20:
        maioridade+=1
    else:
        menoridade+=1
print(f'Dessas 7 pessoas {maioridade} ja atingiram a maior idade e {menoridade} pessoas ainda não atingiram a maior idade')
