# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

lista = []
for i in range(1,5):
    lista.append(input(f'Digite o {i}° nome: '))
random.shuffle(lista)
print(lista)