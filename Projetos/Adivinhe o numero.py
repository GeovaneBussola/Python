from random import randint
from time import sleep
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def verifica_numero(contador,dificuldade):
    while True:
        try:
            tentativa = int(input(f'{contador}° Tentativa: '))
            if tentativa > dificuldade or tentativa < 1:
                print(f'Numero deve ser de [1 - {dificuldade}]')
            else:
                return tentativa
        except ValueError:
            print('Digito invalido')
def verifica_dificuldade():
    while True:
        try:
            dificuldade = int(input('Escolha o nivel de dificuldade:\n[1] Easy (1 - 10)\n[2] Medium (1 - 100)\n[3] Hard (1 - 1000)\n'))
            if dificuldade > 3 or dificuldade <1:
                print('Digito invalido!! Digite o nivel de dificuldade [1], [2] ou [3]')
            else:
                limpar_terminal()
                if dificuldade == 1:
                    print(f'{"-" * 8} Dificuldade \033[32m[Easy]\033[m {"-" * 8}')
                    dificuldade = 10
                elif dificuldade == 2:
                    print(f'{"-" * 8} Dificuldade \033[33m[Medium]\033[m {"-" * 8}')
                    dificuldade = 100
                else:
                    print(f'{"-" * 8} Dificuldade \033[31m[Hard]\033[m {"-" * 8}')
                    dificuldade = 1000
                return dificuldade
        except ValueError:
            print('Digito invalido!! Digite o nivel de dificuldade [1], [2] ou [3]')
def jogar_novamente():
    while True:
        try:
            continuar = int(input('Deseja jogar novamente?\n(0)não\n(1)sim\n'))
            if continuar not in (0,1) :
                print('Digite 0 ou 1')
            else:
                return continuar
        except ValueError:
            print('Digito invalido')
def verificar_tentativas(tentativas):
    while True:
        try:
            verificar=int(input('Deseja verificar suas tentativas?\n(0)não\n(1)sim\n'))
            if verificar not in (0,1):
                print('Digite 0 ou 1')
            else:
                limpar_terminal()
                if verificar == 1:
                    for a, b in tentativas.items():
                        print(f'{a} = {b}')
                    sleep(1.5)
                    break
                else:
                    break
        except ValueError:
            print('Digito invalido')

print('Bem vindo ao minigame!!')
while True:
    tentativas = {}
    contador= 1
    dificuldade = verifica_dificuldade()
    numero = randint(1,dificuldade)
    print(f'Tente acertar um numero de \033[1m1\033[m a \033[1m{dificuldade}\033[m')
    while True:
        tentativa = verifica_numero(contador,dificuldade)
        tentativas[f'{contador}° tentativa'] = tentativa
        if tentativa == numero:
            limpar_terminal()
            print(f'\033[32mVocê acertou, parabéns!!')
            print(f'O numero escolhido foi {numero} e você acertou em {contador} {"tentativa" if contador == 1 else "tentativas"}!!\033[m')
            sleep(1.5)
            print('-' * 35)
            verificar_tentativas(tentativas)
            break
        print('O numero é \033[1m++Maior++\033[m ' , end="") if numero > tentativa else print('O numero é \033[1m--Menor--\033[m ', end="")
        contador+=1
    print('-' * 23)
    if jogar_novamente() ==0:
        limpar_terminal()
        print('Obrigado por jogar (☞ﾟヮﾟ)☞')
        for i in 'Jogo desenvolvido por Geovane':
            print(f'{i}',end="")
            sleep(0.1)
        print()
        break
    else:
        limpar_terminal()
        continue
    
    