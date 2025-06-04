# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
while True:
    primeiro_termo = int(input('Digite o primeiro termo: '))
    razão = int(input('Digite a razão da PA: '))
    contador = 0
    while contador < 10:
        contador+=1
        print(f'{primeiro_termo}, ', end='') if contador < 10 else print(f'{primeiro_termo}', end='')
        primeiro_termo+=razão
    a = int(input('Digite [0] para parar ou [1] para repetir'))
    if a == 0:
        break
    elif a == 1:
        continue
    else:
        print('Digito invalido')