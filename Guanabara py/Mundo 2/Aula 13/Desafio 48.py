# Exercício Python 48: Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for i in range(1,501):
    if i % 2 == 1 or i == 1:
        if i % 3 == 0:
            soma += i
print(soma)