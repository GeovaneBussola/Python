# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maiorpeso = 0
menorpeso = 0
for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso or menorpeso == 0:
        menorpeso = peso
print(f'O maior peso foi {maiorpeso:.0f}Kg e o menor peso foi {menorpeso:.0f}Kg')