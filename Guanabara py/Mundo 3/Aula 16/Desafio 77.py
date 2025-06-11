# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('mascara','amigos','fazenda','chuveiro','manteiga','pastel','churros','praia')

for i in lista:
    print(f'\nNa palavra \033[1m{i}\033[m temos as vogais: ',end='')
    for a in i:
        if a in 'aeiou':
            print(f'{a} ', end='')
    