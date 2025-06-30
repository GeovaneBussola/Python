# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dicionario = {}
nome = input('Nome: ')
media = float(input('Media: '))
dicionario['Nome'] = nome
dicionario['Media'] = media
dicionario['Situação'] = 'Aprovado' if media > 6 else 'reprovado'
print(f'O aluno {dicionario["Nome"]} com a media {dicionario["Media"]} esta {dicionario["Situação"]}')

