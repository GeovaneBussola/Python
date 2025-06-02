# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro: '))
chave = int(input('Digite\n[1] Binario\n[2] Octal\n[3] Hexadecimal\n'))

if chave == 1:
    print(f'{num} Convertido para binario é: {bin(num)[2:]}')
elif chave == 2:
    print(f'{num} Convertido para Octal é: {oct(num)[2:]}')
elif chave == 3:
    print(f'{num} Convertido para Hexadecimal é: {hex(num)[2:]}')
else:
    print('Conversor invalido')
    
        