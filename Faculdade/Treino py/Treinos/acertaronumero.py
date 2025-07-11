from random import *
num = randint(0,10)
contador = 0
while True:
    entrada = int(input('Escolha um numero de 0 a 10: '))
    contador = contador+1
    if entrada == num:
        break
    elif num < entrada:
        print('Você errou! o numero é menor')
    else:
        print('Você errou! o numero é maior')
print(f'Parabéns, você acertou em {contador} tentativas')