# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
while True:
    numero = int(input('Digite um numero inteiro de 0-9999: '))
    if numero < 0 or numero > 9999:
        print('Numero invalido')
    else:
        print(F'Unidade: {numero // 1 % 10}')
        print(F'Dezena: {numero // 10 % 10}')
        print(F'Centena: {numero // 100 % 10}')
        print(F'Milhar: {numero // 1000 % 10}')
            