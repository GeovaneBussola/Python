# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

principal = []
temporario = []
maispesado = 0
maisleve = 0
while True:
    temporario.append(input('Digite o nome da pessoa: '))
    temporario.append(int(input('Digite o peso da pessoa: ')))
    principal.append(temporario[:])
    temporario.clear()
    while True:
        continuar = input('Deseja adicionar mais alguem? [s/n] ').lower().strip()
        if continuar in ('s','n'):
            break
        else:
            print('digito invalido')
    if continuar == 'n':
        break
for i in principal:
    if i[1] == 0 or i[1] > maispesado:
        maispesado = i[1]
    if i[1] == 0 or i[1] < maisleve:
        maisleve = i[1]
