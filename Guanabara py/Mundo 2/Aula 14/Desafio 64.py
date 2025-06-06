# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = contador = 0
while True:
    num = int(input('Digite um numero inteiro ou [999] para parar'))
    if num != 999:
        soma+=num
        contador+=1
    else:
        break
print(f'A soma dos {contador} numeros digitados é {soma}')