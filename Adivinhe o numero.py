from random import randint
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
            dificuldade = int(input('Escolha o nivel de dificuldade:\n[1] easy(1 - 10)\n[2] medium (1 - 100)\n[3] hard (1 - 1000)\n'))
            if dificuldade > 3 or dificuldade <1:
                print('Digito invalido!! Digite o nivel de dificuldade [1], [2] ou [3]')
            else:
                if dificuldade == 1:
                    print('---Dificuldade [Easy]---')
                    dificuldade = 10
                elif dificuldade == 2:
                    print('---Dificuldade [Medium]---')
                    dificuldade = 100
                else:
                    print('---Dificuldade [Hard]---')
                    dificuldade = 1000
                return dificuldade
        except ValueError:
            print('Digito invalido!! Digite o nivel de dificuldade [1], [2] ou [3]')
def jogar_novamente():
    while True:
        try:
            print("-" *30)
            continuar = int(input('Deseja jogar novamente?\n(0)não\n(1)sim\n'))
            print('-' * 30)
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
                if verificar == 1:
                    print('-' * 30)
                    for a, b in tentativas.items():
                        print(f'{a} = {b}')
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
    while True:
        tentativa = verifica_numero(contador,dificuldade)
        tentativas[f'{contador}° tentativa'] = tentativa
        if tentativa == numero:
            print('-' * 30)
            print(f'Você acertou, parabéns!!')
            print(f'O numero era {numero}, você acertou em {contador} tentativa(s)!!')
            print('-' * 30)
            verificar_tentativas(tentativas)
            break
        print('O numero é maior') if numero > tentativa else print('O numero é menor')
        contador+=1
    if jogar_novamente() ==0:
        print('Obrigado por jogar (☞ﾟヮﾟ)☞')
        break
    else:
        continue
    
    