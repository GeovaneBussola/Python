# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*pacote):
    if not pacote:
        print('A lista na possui numeros')
        return
    maior = menor = pacote[0]
    for i in pacote:
        if menor > i:
            menor = i
        if maior < i:
            maior = i
    print(f'O maior é: {maior}')
    print(f'O menor é: {menor}')

maior(4,5,3,3,5,6,4,9,1)




