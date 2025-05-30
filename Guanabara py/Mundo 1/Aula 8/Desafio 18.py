# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo {angulo} tem o seno de {seno:.2f}')
coseno = math.cos(math.radians(angulo))
print(f'O ângulo {angulo} tem o coseno de {coseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo {angulo} tem o tangente de {tangente:.2f}')
