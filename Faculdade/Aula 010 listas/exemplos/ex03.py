# 3- Faça um programa em Python que calcule e mostre a média de uma quantidade
# indeterminada de números inteiros digitados pelo usuário. Para sair o usuário deverá
# digitar 0. Use lista e exiba no final os números digitados.
lista=[]
chave = 1
print('Calculadora de medias para numeros ideterminados. Para calcular a media dos numeros enviados digite "0" (o numero minimo a ser digitado é 1)')
while True:
    while True:

        n = input(f'Digite o {chave}º numero: ')
        if not n.isdigit():
            print('O digito Precisa ser um numero')
            continue
        else:
            n = int(n)
            if n > 10 or n < 0:
                print('O numero precisa ser de "(1-10)"')
                continue
            else:
                break 

    chave+=1
    if not n == 0:
        lista.append(n)   
    if sum(lista) == 0:
        chave-=1
        print('Digite algum numero antes de calcular a media')
        continue

    if n == 0:
        media = sum(lista) / len(lista)
        print(f'A media dos numero digitados é {media:.1f}')
        break


