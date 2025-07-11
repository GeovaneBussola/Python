# Exemplo 2 – método void
# Vamos elaborar um programa em Python que receba um número inteiro e uma
# mensagem e exiba na tela essas informações.

def numero_inteiro_e_mensagem(numero_inteiro,mensagem):
    print(f'{numero_inteiro} {mensagem}')
n=int(input('Digite um numero inteiro: '))
m=input('Digite uma mensagem: ')
numero_inteiro_e_mensagem(n,m)