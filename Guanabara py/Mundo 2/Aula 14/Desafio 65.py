# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
contador = 0
soma = 0
maior = 0
menor = 0
while True:
    num = int(input('Digite um numero: '))
    soma+=num
    contador+=1
    if num > maior:
        maior = num
    if  num < menor or menor == 0:
        menor = num
    continuar = input('Deseja continuar? (s/n) ').strip().lower()
    if continuar == 'n':
        break
print(f'A media de todos valores digitados é {soma / contador:.1f}\nO maior numero foi {maior} e o menor foi {menor}')

    
