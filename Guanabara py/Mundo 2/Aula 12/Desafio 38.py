# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))

if n1 > n2:
    print(f'O {n1} é maior do que o {n2}')
elif n2 > n1:
    print(f'O {n2} é maior do que o {n1}')
else:
    print(f'O {n1} e {n2} são iguais')