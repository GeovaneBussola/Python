# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
tentativa = 0
num = randint(0,10)
while True:
    tentativa+=1
    jogador = int(input('Tente adivinhar um numero inteiro que o computador escolheu entre 0-10 '))
    if jogador == num:
        print('\033[33mParabéns!!! Você acertou.\033[m')
        print(f'Foi necessario {tentativa} tentativa(s) para acertar o numero')
        break
    print('Você errou, tente novamente')
    print('-=' * 15)
    

