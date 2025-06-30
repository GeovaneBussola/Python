# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[],[],[]]

for i in range(3):
    contador=0
    while contador <= 2:
        matriz[i].append(int(input(f'Digite um valor para [{i},{contador}]')))
        contador += 1
for i in matriz:
    for i in i:
        print(f'[{i:^4}]',end='')
    print()


