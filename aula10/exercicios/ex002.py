# Exercício
# 2- Faça um programa que:
# ▪ Leia duas listas com 5 numeros inteiros cada.
# ▪ Checa quais elementos da segunda lista são iguais a algum elemento da primeira
# lista.
# ▪ Se não houver elementos em comum, o programa deve informar isso.
# Entrada 
# [1, 2, 3, 4, 5]
# [0, 7, 6, 10, 3]
# Saída
# 3

# Entrada 
# [1, 2, 3, 4, 5]
# [0, 7, 6, 10, 8]
# Saída
# Não há elemento em comum

import random
lista1=[]
lista2=[]
numeros_em_comum=[]
for i in range(10):
    if len(lista1) < 5:
        lista1.append(random.randint(1,10))
    else:
        lista2.append(random.randint(1,10))

for i in lista1:
    if i in lista2:
        numeros_em_comum.append(i)

if len(numeros_em_comum) == 0:
    print('Não há elemento em comum')
else:
    print('Os elementos em comum são:')
    for i in numeros_em_comum:
        print(f'{i}, ', end='')