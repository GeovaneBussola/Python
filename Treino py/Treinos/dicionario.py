# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionario. No final, mostre o conteudo da estrutura na tela.

aluno = {}
aluno['Nome'] = input('Nome: ').capitalize()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['Situação'] = 'Aprovado' if aluno['Media'] >= 6 else 'Reprovado'

for i, a in aluno.items():
    print(f'{i} é igual a {a}')