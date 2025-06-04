# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:0 – 1 – 1 – 2 – 3 – 5 – 8

contador = 0
t1 = 0
t2 = 1
qtd = int(input('Digite a quantidade de elementos: '))
print(f'Os {qtd} primeiros elementos de uma sequencia de fibonacci com esse numero inteiro são:')
while True:
    contador+=1
    num = t1 + t2
    print(f'{num}, ', end='') if contador < qtd else print(f'{num}')
    t1 = t2
    t2 = num
    if contador == qtd:
        break

    
