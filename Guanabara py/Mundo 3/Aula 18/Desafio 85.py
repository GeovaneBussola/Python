# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista=[[],[]]


for i in range(1,8):
    num = int(input(f'Digite o {i}° valor'))
    if num != 0:
        if num % 2 == 0:
            lista[0].append(num)
        else:
            lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os numero pares digitados foram {lista[0]} e os impares foram {lista[1]}')

