# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Escolha um numero para ver sua tabuada: '))
for i in range(1,11):
    print(f'{num} * {i} = {num * i}')