# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa R$'))
salario = float(input('Digite seu salário R$'))
parcelas = float(input('Digite em quantas anos deseja pagar o emprestimo:'))
parcelas = parcelas * 12 
parcela = casa / parcelas
if parcela > (salario*0.3):
    print('Emprestimo negado')
else:
    print('Emprestimo aceito')




