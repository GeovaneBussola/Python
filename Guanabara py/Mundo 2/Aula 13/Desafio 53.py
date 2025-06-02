# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite a frase: ').strip()
sefrase = frase.replace(' ', '')
contrario=''
for i in sefrase:
    contrario = i + contrario
if sefrase == contrario:
    print(f'A frase \'{frase}\' é um palidromo')
else:
    print('A frase não é um palidormo')
