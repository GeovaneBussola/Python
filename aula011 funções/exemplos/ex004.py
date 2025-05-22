# Exemplo 4 - Método com retorno
# Escreva um método com retorno que receba como parâmetros a base e a altura de um
# triângulo, calcule e retorne o valor de sua área.
# area = base*altura/2
# Faça um programa em Python que solicite a base e altura de um triângulo ao usuário, e
# utilizando a função definida acima, calcule e mostre o valor da área.
# Após o cálculo anterior, defina outros valores no código de base e altura e utilizando o
# mesmo método acima, mostre o valor da área.


def mostrar_area_triangulo(base,altura):
    area= base*altura/2
    return area
base=float(input('Digite a base do triangulo: '))
altura=float(input('Digite a altura do triangulo: '))
print(f'A area do triangulo é: {mostrar_area_triangulo(base,altura):.2f}')

