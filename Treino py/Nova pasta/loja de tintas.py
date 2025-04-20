# Faça um programa em Python para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total.

import math

# Entrada
area = float(input("Digite o tamanho da área a ser pintada (em m²): "))

# Cálculo da quantidade de tinta necessária
litros_necessarios = area / 3

# Cada lata tem 18 litros
latas = math.ceil(litros_necessarios / 18)

# Preço por lata
preco_total = latas * 80

# Saída
print(f"\nVocê precisará de {latas} lata(s) de tinta.")
print(f"Preço total: R${preco_total:.2f}")

