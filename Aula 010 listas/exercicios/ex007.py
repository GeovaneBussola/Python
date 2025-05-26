# 7- Elabore um programa em Python que leia os salários de 10 trabalhadores de uma
# empresa e os armazene em uma lista. Após a entrada de dados, o programa deverá:
# ▪ Calcular a média desses salários.
# ▪ Determinar o maior dos salários desta empresa.
# ▪ Contar os salários menores que R$850,00.
# ▪ Exibir todos os resultados na tela.

salarios=[]
maior_salario = None
menor_salario =0
print('Digite o salario dos funcionarios')
for i in range(1,11):
    salarios.append(float(input(f'{i}° Funcionario: ')))
media = sum(salarios) / len(salarios)
for i in salarios:
    if maior_salario is None or i > maior_salario:
        maior_salario = i
for i in salarios:
    if i < 850:
        menor_salario+=1
print(f'A media dos salarios é: {media:.2f}')
print(f'O maior salario da empresa é: {maior_salario}')
print(f'{menor_salario} salarios são menores que R$850,00')






