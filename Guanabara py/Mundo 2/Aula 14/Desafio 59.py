# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

while True:
    vl1 = float(input('Digite o primeiro valor: '))
    vl2 = float(input('Digite o segundo valor: '))
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Escolha a uma opção: '))
    if escolha == 1:
        print(f'{vl1} + {vl2} = {vl1 + vl2}')
    elif escolha == 2:
        print(f'{vl1} * {vl2} = {vl1 * vl2}')
    elif escolha == 3:
        if vl1 > vl2:
            print(f'{vl1} é o maior valor')
        elif vl2 > vl1:
            print(f'{vl2} é o maior valor')
        else:
            print('Os 2 valores são iguais')
    elif escolha == 4:
        continue
    elif escolha == 5:
        break
    else:
        print('Opção invalida, tente novamente')

    
    
