def verifica_numero(contador):
    while True:
        try:
            tentativa = int(input(f'Tentativa n{contador}: '))
            if tentativa > 10 or tentativa < 0:
                print('Numero deve ser de [1-10]')
            else:
                return tentativa
        except ValueError:
            print('Digito invalido')
from random import randint
tentativas = {}
contador= 1
numero = randint(1,10)
print('Bem vindo ao minigame!!')
print("-" * 30)
print('Tente acertar um numero de 1 a 10')
while True:
    tentativa = verifica_numero(contador)
    tentativas[f'{contador}° tentativa'] = tentativa
    if tentativa == numero:
        print('Você acertou o numero parabéns!!')
        print(f'Acertou o numero em {contador} tentativas, sendo elas:')
        for a, b in tentativas.items():
            print(f'{a} = {b}')
        break
    print('O numero é maior') if numero > tentativa else print('O numero é menor')
    contador+=1
    
    
    