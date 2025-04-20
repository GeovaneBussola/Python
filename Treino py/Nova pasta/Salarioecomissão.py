#Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um
#programa em Python que receba o salário fixo do funcionário e o valor de suas vendas,
#calcule e mostre a comissão e o salário final do funcionário.

salariofixo = float(input("Digite seu salário fixo: "))
vendas = float(input('Digite o valor de suas vendas totais: '))
vendas = vendas *0.04
print(f'Seu salario com a comissão de vendas é: R${salariofixo + vendas:.2f}')