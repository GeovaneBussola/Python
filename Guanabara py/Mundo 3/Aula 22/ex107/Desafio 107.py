# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import Moeda

numero = int(input('Digite um preço:R$'))
print(f'Aumentando o valor R${numero} temos: {Moeda.aumenta(numero,10)}')
print(f'Diminuindo o valor R${numero} temos: {Moeda.reduz(numero,20)}')
print(f'Dobrando o valor R${numero} temos: {Moeda.dobra(numero)}')
print(f'A metade de {numero} é: {Moeda.metade(numero)}')