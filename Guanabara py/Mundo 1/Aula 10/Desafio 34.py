# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salario: '))
if salario > 1250:
    print(f'O aumento foi de R${salario * 0.1:.2f} o novo salario acrecido do aumento é R${salario + (salario * 0.1):.2f}')
else:
    print(f'O aumento foi de R${salario * 0.15:.2f} o novo salario acrecido do aumento é R${salario + (salario * 0.15):2f}')
