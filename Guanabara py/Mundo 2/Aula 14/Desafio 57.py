# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
while True:
    sexo = input('Digite seu sexo (M/F): ').strip().lower()
    if sexo in ['f','m']:
        break
    print('sexo invalido')
print('Sexo valido')