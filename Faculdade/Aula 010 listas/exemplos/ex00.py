# Faça um programa em Python que leia os doze salários recebidos por um funcionário
# durante um ano, calcule e exiba na tela quanto ele receberá de 13º salário e 1/3 de férias.
# Para os cálculos, utilize as seguintes definições:
# O 13º salário deverá ser igual à média dos salários recebidos no ano.
# Para o cálculo de 1/3 de férias, faça a média dos salários * 1/3.
# Obs.: 1- Obrigatório utilizar alguma estrutura de repetição
# 2- Identificar o mês (Ex: Qual o salário recebido em Jan: R$ )

salarios=[]
mes = ['janeiro', 'fevereiro', 'março','abrilo', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
for i in mes:
    salario = float(input(f'Digite o salario do mes de {i}:R$ '))
    salarios.append(salario)
decimoterceiro = sum(salarios)/len(salarios)
ferias = decimoterceiro * (1/3)

print(f'Decimo terceiro: {decimoterceiro:.2f} \n Ferias: {ferias:.2f}')