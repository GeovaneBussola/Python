# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print(f'{hypot(co,ca):.2f}')
