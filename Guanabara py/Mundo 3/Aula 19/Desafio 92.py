# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados={}

dados['Nome'] = input('Digite o nome: ').strip().capitalize()
dados['Idade'] = date.today().year - int(input('Digite o ano de nascimento: '))
dados['Carteira De Trabalho'] = int(input('Digite o numero da carteira de trabalho (0 não tem): '))
if dados['Carteira De Trabalho'] == 0:
    dados['Carteira De Trabalho'] = 'Desempregado'
else:
    dados['Ano De Contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o salário: '))
    dados['Aposentadoria']= dados['Idade'] + (dados['Ano De Contratação'] + 35 - date.today().year)
for k,i in dados.items():
    print(f'{k} é igual a {i}')