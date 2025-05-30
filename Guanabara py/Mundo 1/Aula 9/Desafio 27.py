# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome: ')).strip()

print(f'first name:{nome.split()[0]}\nLast name:{nome.split()[-1]}')