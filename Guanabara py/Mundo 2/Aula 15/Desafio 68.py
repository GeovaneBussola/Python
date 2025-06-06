# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = computadorvalor = 0
print('=-' * 15)
print('Vamos jogar par ou impar')
print('=-' * 15)

while True:
    computador = randint(0,10)
    valor = int(input('Escolha um valor: '))
    parimpar = input('Par ou impar?').upper().strip()
    soma = computador + valor
    if soma == 0:
        continue
    if parimpar in ['P','PAR']:
        if soma % 2 == 0:
            vitorias+=1
        else:
            computadorvalor = 1
           
    elif parimpar in ['I','IMPAR']:
        if soma % 2 == 0:
            computadorvalor = 1
        else:
            vitorias+=1 
    print(f'O computador jogou {computador} e você jogou {valor} deu {soma} que é {"par" if soma %2 == 0 else "impar"}. ', end='')
    if computadorvalor == 1:
        print('Você PERDEU!!!')
        if vitorias == 0:
            print('Você não venceu nenhuma vez ;-;')
        elif vitorias == 1:
            print('Você venceu uma vez :)')
        else:
            print(f'Você venceu {vitorias} vezes ヾ(^▽^*)))')
        break
    else:
        print('Você VENCEU!!')
        print('Vamos jogar novamente...')