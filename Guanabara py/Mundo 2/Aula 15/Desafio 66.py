# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = contador = 0
while True:
    num = int(input('Digite um numero ou (999) para parar: '))
    if num != 999:
        contador+=1
        soma+=num
    else:
        break
print(f'Foram digitados {contador} numeros e a soma deles é {soma}')
