# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))

menor = a
maior = a

if b < menor and b < c:
    menor = b
elif c < b and c < a:
    menor = c
if b > maior and b > c:
    maior = b
elif c > b and c > maior:
    maior = c
print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')