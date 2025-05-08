#Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores
#são positivos e quantos são negativos. Determine, também, qual é o menor desses
#valores. Utilize o comando de repetição que desejar.

negativo = 0
positivo = 0
menornumero=None
maiornumero =None
numeros = int(input('Digite quantos numeros Você deseja escrever: '))
for i in range(1, numeros + 1):
    numero = int(input(f'Gigite o {i} numero: '))
    
    if menornumero is None or numero < menornumero:
        menornumero = numero
    if maiornumero is None or numero > maiornumero:
        maiornumero = numero
    if numero <0:
        negativo+=1
    else:
        positivo+=1

print(f"Você digitou {negativo} numeros negativos, {positivo} numeros positivos e o menor numero digitado foi {menornumero} e o maior foi {maiornumero}")

        
    
