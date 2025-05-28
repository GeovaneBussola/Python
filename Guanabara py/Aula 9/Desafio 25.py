# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite um nome completo: ')).strip()
nome = True if 'silva' in nome.lower() else False
print(nome)