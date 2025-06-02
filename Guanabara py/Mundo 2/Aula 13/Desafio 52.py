# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
num = int(input('Digite um numero para saber se ele é primo: '))
for i in range(1,num+1):
    if num % i == 0:
        tot+=1
if tot == 2:
    print('O numero é primo')
else:
    print('O numero não é primo')

    