# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
alunos = []
for i in range(1,5):
    alunos.append(input(f'Digite o {i}° aluno: '))
print(f'O aluno escolhido foi {random.random(alunos)}')