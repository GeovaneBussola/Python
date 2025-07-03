# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(largura,comprimento):
    área = largura * comprimento
    print(f'O terreno com comprimento de {comprimento} e largura de {largura} tem {área} de área')

l=float(input('Largura do terreno: '))
c=float(input('Comprimento do terreno: '))

área(l,c)