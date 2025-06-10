# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
def l():
    print('-'*30)
a = (int(input('Digite um numero')),
     int(input('Digite um numero')),
     int(input('Digite um numero')),
     int(input('Digite um numero')),)
l()
print(f'O 9 aparace {a.count(9)} veze(s)')
l()
if 3 in a:
    print(f'O primeiro 3 aparece na posição {a.index(3)}') 
else:
    print('Não tem 3 na tupla')
l()
print('Os numeros pares foram ' , end="")
for i in a:
    if i % 2 == 0:
        print(f'{i}, ' , end="" if i != a[-1] else f'{i}.') 
        


