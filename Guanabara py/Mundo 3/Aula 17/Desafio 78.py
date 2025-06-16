# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
mairvl=0
menorvl=0
for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
print('-='*10)
print(f'A lista é: {lista}')
print(f'O maior valor digitado foi {max(lista)} {"nas posições" if lista.count(max(lista)) > 1 else "na posição"}: ' ,end='')
for a,i in enumerate(lista):
    if i == max(lista):
        print(f'{a}...', end='')
print(f'\nO menor valor digitado foi {min(lista)} {"nas posições" if lista.count(min(lista)) > 1 else "na posição"}: ' ,end='')
for a,i in enumerate(lista):
    if i == min(lista):
        print(f'{a}...', end='')



