# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
contador = 0
while contador < 10:
    contador+=1
    print(f'{primeiro_termo}, ', end='') if contador < 10 else print(f'{primeiro_termo}', end='')
    primeiro_termo+=razão
