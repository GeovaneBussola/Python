# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

lista=[]
dicionario={}
listamulheres=[]

while True:
    dicionario['Nome'] = input('Nome: ').strip().capitalize()
    while True:
        sexo = input('Sexo (M/F)').upper().strip()
        if sexo not in ['M','F']:
            print('\033[31mSexo invalido\033[m')
            continue
        dicionario['Sexo'] = sexo
        break
    dicionario['Idade'] = int(input('Idade: '))
    lista.append(dicionario.copy())
    dicionario.clear()
    continuar = input('Adicionar mais alguem? (S/N) ').strip().upper()
    if continuar == 'N':
        break
print(15*'-=')
print(f'{len(lista)} pessoas foram cadastradas')
mediaidade=0
for i in lista:
    mediaidade+=i['Idade']
mediaidade = mediaidade / len(lista)
print(f'A media de idade é {mediaidade:.0f} anos')
for i in lista:
    if i['Sexo'] == 'F':
        listamulheres.append(i['Nome'])
print(f'Listagem de mulheres: {listamulheres}')
print('Pessoas que estão acima da média de idade:')
for i in lista:
    if i['Idade'] > mediaidade:
        print(i)
