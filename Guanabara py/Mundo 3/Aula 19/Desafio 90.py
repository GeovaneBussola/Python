# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dicionario = {}
dicionario['Nome'] = input('Nome: ')
dicionario['Media'] = float(input('Media: '))
dicionario['Situação'] = 'Aprovado' if dicionario['Media'] > 6 else 'reprovado'
print('-' * 30)
for k,v in dicionario.items():
    print(f'{k} é igual a {v}')

