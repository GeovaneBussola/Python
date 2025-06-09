# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

mais18 = 0
homens = 0
mulheresmenos20 = 0 
while True:
    continuar = ''
    sexo = ''
    print("=-" * 10)
    print('CADASTRE UMA PESSOA')
    print("=-" * 10)
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        mais18+=1
    while sexo not in ['m','masculino','feminino','f']:
        sexo = input('Digite o sexo da pessoa [masculino/feminino]: ').lower().strip()
    if sexo in ['m','masculino']:
        homens+=1
    elif sexo in ['feminino','f']:
        if idade < 20:
            mulheresmenos20 += 1
    while continuar not in ['sim','s','não','n','nao']:
        continuar = input('Deseja continuar [s/n]? ').lower().strip()
    if continuar in ['n','não', 'nao']:
        break
print(f'''{mais18} Pessoas têm mais de 18 anos
{homens} Homens foram cadastrados
{mulheresmenos20} Mulheres têm menos de 20 anos''')
        
        
