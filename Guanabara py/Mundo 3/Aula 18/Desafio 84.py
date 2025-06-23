# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

principal = []
temporario = []
pessoascadastradas = 0
while True:
    temporario.append(input('Digite o nome da pessoa: '))
    temporario.append(int(input('Digite o peso da pessoa: ')))
    principal.append(temporario[:])
    temporario.clear()
    pessoascadastradas += 1
    while True:
        continuar = input('Deseja adicionar mais alguem? [s/n] ').lower().strip()
        if continuar in ('s','n'):
            break
        else:
            print('digito invalido')
    if continuar == 'n':
        break
maispesado=principal[0][1]
maisleve=principal[0][1]
for i in principal:
    if i[1] > maispesado:
        maispesado = i[1]
    if i[1] < maisleve:
        maisleve = i[1]
print(f'O maior peso cadastrado foi de {maispesado}. Peso de ')
for i in principal:
    if i[1] == maispesado:
        print(f'[{i[0]}] ')
print(f'O menor peso cadastrado foi de {maisleve}. Peso de ')
for i in principal:
    if i[1] == maisleve:
        print(f'[{i[0]}]')
print(f'E foi cadastradas no total {pessoascadastradas} pessoa[s]')

