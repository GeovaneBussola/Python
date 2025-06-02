# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

vlproduto = float(input('Digite o valor do produto: '))
pagamento = int(input('Digite a forma de pagamento\n[1] - à vista dinheiro/cheque: 10% de desconto\n[2] - à vista no cartão: 5% de desconto\n[3] - em até 2x no cartão: preço formal\n[4] - 3x ou mais no cartão: 20% de juros\n'))
if pagamento == 1:
    preço = vlproduto - (vlproduto*0.1)
elif pagamento == 2:
    preço = vlproduto - (vlproduto*0.05)
elif pagamento == 3:
    preço = vlproduto
elif pagamento == 4:
    preço = vlproduto + (vlproduto*0.2)
print(f'O preço a ser pago é R${preço:.2f}')
