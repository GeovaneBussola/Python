# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[],[],[]]
par=terceiracoluna=0
for i in range(3):
    contador=0
    while contador <= 2:
        matriz[i].append(int(input(f'Digite um valor para [{i},{contador}]')))
        contador += 1
print('-=' * 18)
for i in range(3):
    for j in range(3):
        valor=matriz[i][j]
        print(f'[{valor:^5}]',end='')
        if valor % 2 == 0:
            par+=valor
        if j == 2:
            terceiracoluna+=valor
    print()
print('-=' * 18)
print(f'A soma de todos valores pares digitados é {par}')
print(f'A soma dos valores da terceira coluna é {terceiracoluna}')
print(f'O maior valor digitado na segunda linha é {max(matriz[1])}')