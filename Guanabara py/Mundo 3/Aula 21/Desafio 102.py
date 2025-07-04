# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num,show=0):
    resultado = 1
    for i in range(num,0,-1):
        if show == True:
            print(f'{i} ',end='')
            print(f'{"x " if i != 1 else "= "}',end='')
        resultado*=i
    print(resultado)

fatorial(4,True)