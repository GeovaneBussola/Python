# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))

if a + b > c and b + c > a and a + c > b:
    print('Pode formar um tringulo')
else:
    print('Nao pode formar um trigandulo')