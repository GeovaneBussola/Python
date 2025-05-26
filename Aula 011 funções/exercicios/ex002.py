# 2- Escreva um método com retorno que receba como parâmetros os lados de um
# retângulo, calcula e retorna o valor de sua área.
# area = lado*lado
# Faça um programa principal que solicite os valores dos lados de um retângulo ao usuário,
# e utilizando a função definida acima, calcule e mostre o valor de área.

calculo_area_retangulo = lambda base,altura: base * altura

base = float(input('Digite a base do retangulo: '))
altura = float(input('Digite a altura do retangulo: '))
print(f'A area do retangulo é: {calculo_area_retangulo(base,altura):.2f}')

