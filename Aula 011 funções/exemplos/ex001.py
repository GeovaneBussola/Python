# Exemplo 1 – soma de inteiros
# Vamos elaborar um programa em Python que receba dois números inteiros, calcule e
# exiba na tela a soma desses números.

def soma_inteiros(a,b):
    a = a + b
    print(a)

n1 = int(input('Digite o 1° numero inteiro: '))
n2 = int(input('Digite o 2° numero inteiro: '))
soma_inteiros(n1,n2)