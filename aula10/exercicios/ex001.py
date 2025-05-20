# 1- Faça um programa em Python que contenha 3 listas com os nomes: valores, par e
# impar. Solicite N números inteiros ao usuário e armazene-os na lista chamada valores
# (utilize como critério de parada se o usuário deseja continuar).
# ▪ Após a obtenção dos dados, na lista par armazene apenas os números pares da lista
# valores e na lista ímpar os números ímpares. É obrigatório o uso de estrutura de
# repetição e listas.
# ▪ Exiba os números armazenados nas 3 listas.

valores=[]
par=[]
impar=[]
print('Digite um numero inteiro ou (x para parar): ')
while True:
    nint=input()
    if nint == 'x':
        break
    else:
        nint=int(nint)
        valores.append(nint)
    
for i in valores:
    if (i%2) == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'Valores: {valores}')
print(f'Par: {par}')
print(f'Impar: {impar}')








