# Faça um programa em Python que recebe a idade de cada um dos 500 alunos de uma
# escola, matriculados no Ensino Médio. O algoritmo deverá verificar, calcular e imprimir:
# a) a quantidade de alunos que podem votar, ou seja, têm idade mínima de 16 anos.
# b) a média da idade dos alunos que não são eleitores.

alunos = 500
naoeleitor = 0
contador = 0
for i in range(1,alunos + 1):
    idade = int(input('Digite a idade do aluno: '))
    if idade <16:
        naoeleitor+=idade
        contador+= 1
print(f'A quantidade de alunos que podem votar é {alunos - contador}')
print(f'A media da idade dos alunos que não podem votar é {naoeleitor / contador}')
    
